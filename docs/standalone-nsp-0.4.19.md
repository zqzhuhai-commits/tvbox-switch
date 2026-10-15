# SwitchTVBox 0.4.19 — 独立 NSP 测试包

使用用户提供的官方 v0.4.19 NRO 重新封装为独立 NSP，保留名称、图标与内置资源。不是原作者的官方 NSP 发布。

## 下载

[下载 SwitchTVBox-0.4.19-standalone-test.nsp](https://github.com/zqzhuhai-commits/tvbox-switch/releases/download/v0.4.19-nsp-test/SwitchTVBox-0.4.19-standalone-test.nsp)

文件大小：38,616,280 字节。Title ID：`05d7c55b04190000`。

SHA-256：`4b30466f34066f4f9894a5b91e803e00c549151ecb672b71964021c59fd827f5`。

## 打包方法和验证

将 NRO 的三个程序段保留原始字节，封装为 NSO；将原 NRO 的 177 个 RomFS 文件、图标和 NACP 元数据放入独立安装包。设计为直接从 HOME 菜单启动，不依赖外部 NRO。

已验证 NSP/PFS0 结构、三个 NCA 文件哈希、NCA 文件系统头、1,280 个完整性块、CNMT 内容记录、NSO 程序段和全部 177 个资源文件。

**未经过 Switch 真机安装、启动或播放测试，不能保证兼容你的系统。** 原程序的 NRO 更新/重启功能可能不适用于此独立包；后续更新应重新打包验证。

本仓库不包含客户端源码。运行功能由原始二进制提供，本次只处理封装；原程序的授权与权利归原权利人所有。

## 来源

- 原项目：https://github.com/zender555/SwitchTVBox
- 原版本：https://github.com/zender555/SwitchTVBox/releases/tag/v0.4.19
- 原 NRO SHA-256：`5e96c98397f2cad274dae5809bca0127d2d48a598066a38cff85b4c5eb4a030f`
- NSO 结构参考：https://github.com/switchbrew/switch-tools/blob/master/src/elf2nso.c
- libnx 双格式入口：https://github.com/switchbrew/libnx/blob/master/nx/source/runtime/switch_crt0.s

文件中没有加入用户的密钥文件、登录信息或 SD 卡配置。

## 传输与发布

`payload/*.part` 是测试包的 gzip 分块，由 GitHub Actions 自动合并、校验 SHA-256 并发布到 Releases。下载 NSP 时请使用上面的 Releases 链接，不要安装分块文件。

也可以下载整个仓库后运行 `python3 scripts/assemble.py`，在仓库根目录还原同一份 NSP。
