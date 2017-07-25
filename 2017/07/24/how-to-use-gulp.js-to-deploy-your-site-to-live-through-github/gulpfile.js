var gulp   = require('gulp');
var deploy = require('gulp-gh-pages');

gulp.task('deploy', function () {
  return gulp.src("./prod/**/*")
    .pipe(deploy({ 
      remoteUrl: "https://github.com/your_github_username_here/your_github_username_here.github.io.git",
      branch: "master"
    }))
});