lz4 decompress .lz4 to dll with single file o multiples files inside dir


### Intro
Xamarin applications, after unpack have a directory called *assemblies*, inside that directory 2 files exists:

* assemblies.blob
* assemblies.manifest

This is how Xamarin packs DLLs. to unpack assemblies.blob files use this tool [https://github.com/jakev/xamarin-assembly-store-unpack](https://github.com/jakev/xamarin-assembly-store-unpack) thanks @javek O/.


After use *xamarin-assembly-store-unpack* you can run this script in just one DLL, or in a directory with several DLL's.


#### Requirements

```bash

python3 -m pip install lz4

```

### Usage:
```python3
python3 lz4_decompress_py3.py -d test_dir #test_dir with .lz4 inside

or 

python3 python3 lz4_decompress_py3.py -s Xamarin.AndroidX.AppCompat.dll

```


Thanks: @securitygrind
