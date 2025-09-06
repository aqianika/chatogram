[app]

# Application title
title = SecureChat Pro

# Package name (no spaces, lowercase)
package.name = securechatpro

# Package domain (reverse domain format)
package.domain = com.securechat

# Source directory
source.dir = .

# Source files to include
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf

# Source patterns to include
source.include_patterns = assets/*,images/*,fonts/*,*.kv

# Application version
version = 1.0

# Application version code (integer)
version.code = 1

# Author name
author = SecureChat Team

# Application requirements (SIMPLIFIED - ONLY ESSENTIAL)
requirements = 
    python3,
    kivy==2.2.0,
    requests==2.31.0

# Android permissions (MINIMAL - ONLY INTERNET)
android.permissions = 
    INTERNET,
    ACCESS_NETWORK_STATE

# Android API target
android.api = 33

# Android minimum API
android.minapi = 21

# Android SDK version
android.sdk = 33

# Android NDK version (LATEST STABLE)
android.ndk = 25b

# Android architectures to build for
android.arch = arm64-v8a, armeabi-v7a

# Orientation
orientation = portrait

# Fullscreen mode
fullscreen = 0

# Window orientation
window.orientation = portrait

# Log level
log_level = 2

# Presplash screen
presplash.filename = %(source.dir)s/assets/presplash.png
presplash.color = #2962FF

# Application icon
icon.filename = %(source.dir)s/assets/icon.png

# Bootstrap
android.bootstrap = sdl2

# Graphics backend
graphics = opengl_es2

# Accelerated graphics
graphics.accelerated = 1

# Multisampling
graphics.multisamples = 2

# Touchscreen support
input.touchscreen = 1

# Mouse support
input.mouse = 0

# Debug mode
debug = 1

# Release mode
release = 0

# Java source directory
source.javacode_dir = src

# Android additional libraries
android.add_libs_arm64_v8a = 
android.add_libs_armeabi_v7a = 

# Android additional AARs
android.add_aars = 

# Android additional JARs
android.add_jars = 

# Android additional resources
android.add_res_directories = 

# Android additional assets
android.add_assets_directories = 

# Android manifest activities
android.manifest_activities = 

# Android intent filters
android.intent_filters = 

# Android metadata
android.meta_data = 

# Android features
android.features = 

# Android gradle dependencies
android.gradle_dependencies = 

# Android packaging options
android.packaging_options = 

# Android compile options
android.compile_options = 

# Android aapt options
android.aapt_options = 

# Android dependencies
android.dependencies = 

# Android FCM (disabled)
android.fcm_enable = 0

# Android x86 build (disabled for smaller size)
android.allow_x86 = 0

# Android service
android.service = 

# Android backup
android.allow_backup = true

# Android large heap
android.large_heap = false

# Android extract assets
android.extract_assets = true

# Android overrides
android.overrides = 

# Android no strip
android.no_strip = 

# Android static libraries
android.static_libraries = 

# Android copy libraries
android.copy_libs = 1

# Android wildcard permissions
android.wildcard_permissions = 0

# Android minimum SDK version
android.min_sdk_version = 21

# Android target SDK version
android.target_sdk_version = 33

# Android update project
android.update_project = 1

# Android signing
android.release_artifact = .apk
android.debug_artifact = .apk

# Android keystore (for release - COMMENTED)
# android.keystore = 
# android.keystore_password = 
# android.keyalias = 
# android.keyalias_password = 

# iOS settings (IGNORE FOR ANDROID)
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.arch = arm64
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.7.0

# Cython compiler directives
cython.compiler_directives = 
    language_level=3,
    boundscheck=False,
    wraparound=False

# Cython include directories
cython.include_dirs = 

# Cython exclude patterns
cython.exclude_patterns = 

# Cython extra options
cython.extra_options = 

# Build hooks
pre_build_hook = 
post_build_hook = 

# Clean build
clean_build = 0
clean_dists = 0

# Buildozer URL
buildozer.url = https://github.com/kivy/buildozer

# Python-for-Android URL
p4a.url = https://github.com/kivy/python-for-android
p4a.branch = master

# P4A local recipes
p4a.local_recipes = 

# P4A extra options
p4a.extra_options = 

# P4A app theme
p4a.app_theme = 

# P4A app icon
p4a.app_icon = 

# P4A app presplash
p4a.app_presplash = 

# P4A app orientation
p4a.app_orientation = portrait

# P4A app permissions
p4a.app_permissions = 

# P4A app features
p4a.app_features = 

# P4A app intent filters
p4a.app_intent_filters = 

# P4A app metadata
p4a.app_meta_data = 

# P4A app activities
p4a.app_activities = 

# P4A app services
p4a.app_services = 

# P4A app receivers
p4a.app_receivers = 

# P4A app providers
p4a.app_providers = 