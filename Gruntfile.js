module.exports = function (grunt) {

  'use strict';

  grunt.initConfig({
    watch: {
      files: ["hobbycoding/static/less/*.less", "hobbycoding/static/js/base.js"],
      tasks: ["less", "uglify"]
    },
    /* LESS Compile */
    less: {
      development: {
        options: {
          compress: false
        },
        files: {
          "hobbycoding/static/css/base.css": "hobbycoding/static/less/base.less",
        }
      },
      production: {
        options: {
          compress: true
        },
        files: {
          "hobbycoding/static/css/base.css": "hobbycoding/static/less/base.less",
        }
      }
    },
    /* Javascript Uglify */
    uglify: {
      options: {
        mangle: true,
        preserveComments: 'some'
      },
      my_target: {
        files: {
          //'dist/js/app.js': ['static/js/app.js']
        }
      }
    },
    /* Image Compression */
    image: {
      dynamic: {
        files: [{
          expand: true,
          cwd: 'static/img/',
          src: ['**/*.{png,jpg,gif,svg,jpeg}'],
          dest: '/hobbycoding/static/img/'
        }]
      }
    },

// Validate JS code
    jshint: {
      options: {
        jshintrc: '.jshintrc'
      },
      core: {
        src: '/hobbycoding/static/js/app.js'
      }
    },

    csslint: {
      options: {
        csslintrc: '/hobbycoding/static/less/.csslintrc'
      },
      dist: [
        '/hobbycoding/static/css/base.css',
      ]
    },

    /* Compression 전 이미지 삭제 */
    clean: {
      build: ["static/img/*"]
    }
  });

  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-image');
  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-contrib-csslint');

  grunt.registerTask('default', ['watch']);
};
