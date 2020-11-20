# -*- mode: python ; coding: utf-8 -*-
import platform
import subprocess

block_cipher = None

binaries = []
if platform.system() == 'Windows':
    binaries = [("libusb-1.0.dll", ".")]
elif platform.system() == 'Linux':
    binaries = [("/lib/x86_64-linux-gnu/libusb-1.0.so.0", ".")]
elif platform.system() == 'Darwin':
    find_brew_libusb_proc = subprocess.Popen(['brew', '--prefix', 'libusb'], stdout=subprocess.PIPE)
    libusb_path = find_brew_libusb_proc.communicate()[0]
    binaries = [(libusb_path.rstrip().decode() + "/lib/libusb-1.0.dylib", ".")]

a = Analysis(['trezorCliTool.py'],
             binaries=binaries,
             datas=[],
             hiddenimports=['image','pkg_resources.py2_warn'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
        a.scripts,
        [],
        exclude_binaries=True,
        name='macTrezorTool',
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        console=True )
coll = COLLECT(exe,
             a.binaries,
             a.zipfiles,
             a.datas,
             strip=False,
             upx=True,
             upx_exclude=[],
             name='macTrezorTool')
