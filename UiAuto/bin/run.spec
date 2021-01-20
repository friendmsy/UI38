# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['run.py'],
             pathex=['E:\\software\\python3.5.1\\Lib\\site-packages\\xlrd', 'E:\\software\\python3.5.1\\Lib\\site-packages\\logging', 'E:\\software\\python3.5.1\\Lib\\site-packages\\yaml', 'E:\\software\\python3.5.1\\Lib\\site-packages\\win32', 'E:\\software\\python3.5.1\\Lib\\site-packages\\win32com', 'E:\\software\\python3.5.1\\Lib\\site-packages\\requests', 'E:\\software\\python3.5.1\\Lib\\site-packages\\selenium', 'E:\\software\\python3.5.1\\Lib\\site-packages\\pymysql', 'E:\\software\\python3.5.1\\Lib\\site-packages\\xlutils', 'E:\\software\\python3.5.1\\Lib\\site-packages\\xlwt', 'E:\\software\\python3.5.1\\Scripts', 'E:\\software\\python3.5.1\\UiAuto\\common\\my_unittest.py', 'E:\\software\\python3.5.1\\UiAuto\\common\\general.py', 'E:\\software\\python3.5.1\\UiAuto\\common\\log.py', 'E:\\software\\python3.5.1\\UiAuto\\page\\order_page.py', 'E:\\software\\python3.5.1\\UiAuto\\bin'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='run',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
