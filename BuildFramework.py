#-*- coding: UTF-8 -*-

import os


# framework 的名字
FrameworkName = 'MakeFrameWork'
# 编译的路径
Build_Path = '/Users/SXJH/Desktop/MakeFrameWork'

DEVICE_DIR='%s/build/Release-iphoneos/%s.framework'%(Build_Path,FrameworkName)

SIMULATOR_DIR='%s/build/Release-iphonesimulator/%s.framework'%(Build_Path,FrameworkName)

# 编译
os.chdir('%s'%Build_Path)
os.system('xcodebuild -configuration "Release" -target %s -sdk iphoneos clean build'%(FrameworkName))
os.system('xcodebuild -configuration "Release" -target %s -sdk iphonesimulator clean build'%(FrameworkName))


# 创建一个通用文件夹
UniversalPath = '%s/Universal'%(Build_Path)
os.system('mkdir -p %s'%(UniversalPath))
os.system('cp -R %s/ %s/'%(DEVICE_DIR,UniversalPath))

# 合并
os.system('lipo -create %s/%s %s/%s -output %s/Universal/%s'%    (DEVICE_DIR,FrameworkName,SIMULATOR_DIR,FrameworkName,Build_Path,FrameworkName))
os.system('open .')
