////////////////////////////////
// Setup
////////////////////////////////

// Gulp and package
const { src, dest, parallel, series, watch } = require('gulp');
const pjson = require('./package.json');

// Plugins
const autoprefixer = require('autoprefixer');
const browserSync = require('browser-sync').create();
const concat = require('gulp-concat');
const tildeImporter = require('node-sass-tilde-importer');
const cssnano = require('cssnano');
const pixrem = require('pixrem');
const plumber = require('gulp-plumber');
const postcss = require('gulp-postcss');
const reload = browserSync.reload;
const rename = require('gulp-rename');
const sass = require('gulp-sass')(require('sass'));
const spawn = require('child_process').spawn;
const uglify = require('gulp-uglify-es').default;

// Relative paths function
function pathsConfig(appName) {
  this.app = `./${pjson.name}`;
  const vendorsRoot = 'node_modules';

  return {
    vendorsJs: [
      `${vendorsRoot}/@popperjs/core/dist/umd/popper.js`,
      `${vendorsRoot}/bootstrap/dist/js/bootstrap.js`,
    ],
    app: this.app,
    templates: `${this.app}/templates`,
    css: `${this.app}/static/css`,
    sass: `${this.app}/static/sass`,
    fonts: `${this.app}/static/fonts`,
    images: `${this.app}/static/images`,
    js: `${this.app}/static/js`,
  };
}

const paths = pathsConfig();

////////////////////////////////
// Tasks
////////////////////////////////

// Styles autoprefixing and minification
const processCss = [
  autoprefixer(), // adds vendor prefixes
  pixrem(), // add fallbacks for rem units
];

const minifyCss = [
  cssnano({ preset: 'default' }), // minify result
];

function project_styles() {
  return src(`${paths.sass}/project.scss`)
    .pipe(
      sass({
        importer: tildeImporter,
        includePaths: [paths.sass],
      }).on('error', sass.logError),
    )
    .pipe(plumber()) // Checks for errors
    .pipe(postcss(processCss))
    .pipe(dest(paths.css))
    .pipe(rename({ suffix: '.min' }))
    .pipe(postcss(minifyCss)) // Minifies the result
    .pipe(dest(paths.css));
}

function admin_styles() {
  return src(`${paths.sass}/admin.scss`)
    .pipe(
      sass({
        importer: tildeImporter,
        includePaths: [paths.sass],
      }).on('error', sass.logError),
    )
    .pipe(plumber()) // Checks for errors
    .pipe(postcss(processCss))
    .pipe(dest(paths.css))
    .pipe(rename({ suffix: '.min' }))
    .pipe(postcss(minifyCss)) // Minifies the result
    .pipe(dest(paths.css));
}

// Javascript minification
function scripts() {
  return src([`${paths.js}/project.js`, `${paths.js}/*-page.js`])
    .pipe(plumber()) // Checks for errors
    .pipe(uglify()) // Minifies the js
    .pipe(rename({ suffix: '.min' }))
    .pipe(dest(paths.js));
}

// Vendor Javascript minification
function vendorScripts() {
  return src(paths.vendorsJs, { sourcemaps: true })
    .pipe(concat('vendors.js'))
    .pipe(dest(paths.js))
    .pipe(plumber()) // Checks for errors
    .pipe(uglify()) // Minifies the js
    .pipe(rename({ suffix: '.min' }))
    .pipe(dest(paths.js, { sourcemaps: '.' }));
}

// Run django server
function runServer(cb) {
  const cmd = spawn('python', ['manage.py', 'runserver'], { stdio: 'inherit' });
  cmd.on('close', function (code) {
    console.log('runServer exited with code ' + code);
    cb(code);
  });
}

// Browser sync server for live reload
function initBrowserSync() {
  browserSync.init(
    [`${paths.css}/*.css`, `${paths.js}/*.js`, `${paths.templates}/*.html`],
    {
      // https://www.browsersync.io/docs/options/#option-open
      // Disable as it doesn't work from inside a container
      open: false,
      // https://www.browsersync.io/docs/options/#option-proxy
      proxy: {
        target: 'ui:8000',
        proxyReq: [
          function (proxyReq, req) {
            // Assign proxy 'host' header same as current request at Browsersync server
            proxyReq.setHeader('Host', req.headers.host);
          },
        ],
      },
      // https://browsersync.io/docs/options/#option-notify
      notify: false,
    },
  );
}

// Watch
function watchPaths() {
  watch(`${paths.sass}/*.scss`, project_styles);
  watch(`${paths.sass}/*.scss`, admin_styles);
  watch(`${paths.templates}/**/*.html`).on('change', reload);
  watch([`${paths.js}/*.js`, `!${paths.js}/*.min.js`], scripts).on(
    'change',
    reload,
  );
}

// Generate all assets
const generateAssets = parallel(
  project_styles,
  admin_styles,
  scripts,
  vendorScripts,
);

// Set up dev environment
const dev = parallel(initBrowserSync, watchPaths);

exports.default = series(generateAssets, dev);
exports['generate-assets'] = generateAssets;
exports['dev'] = dev;
