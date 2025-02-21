[![Shadowrocket](https://socialify.git.ci/LOWERTOP/Shadowrocket/image?custom_description=%E4%BD%BF%E7%94%A8%E6%89%8B%E5%86%8C+%E4%B8%8E+%E6%87%92%E4%BA%BA%E9%85%8D%E7%BD%AE%0AManual+%26+Configs&description=1&font=Rokkitt&forks=1&logo=https%3A%2F%2Fraw.githubusercontent.com%2FLOWERTOP%2FShadowrocket-First%2Frefs%2Fheads%2Fmain%2Fimg%2FShadowrocket.png&name=1&pattern=Plus&stargazers=1&theme=Light)](https://lowertop.github.io/Shadowrocket "发布页面")

[![README in English](https://img.shields.io/static/v1?label=&message=README%20in%20English&color=blue&logo=googletranslate&logoColor=white&labelColor=blue&messageColor=white)](https://translate.google.com/translate?hl=en&sl=zh-CN&tl=en&u=https://lowertop.github.io/Shadowrocket "Google Translate")

> [!NOTE]
> 
> 原懒人系列配置文件及关键词列表的仓库因故失活，本仓将在其最终版本的基础上进行持续维护，以确保懒人系列配置文件和 Shadowrocket 使用手册的正常使用。如需进一步支持，请参阅 [配色与配置仓库](https://github.com/LOWERTOP/Shadowrocket-First) 或移步 [官方群组](https://t.me/ShadowrocketApp)<br>
> [Johnshall 仓库](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever) 提供的版本也将以本仓文件为基础继续更新。本仓以普通用户的身份对原作者及 [Johnshall](https://github.com/Johnshall) 等所有对相关项目做出贡献的人表示由衷的感谢！

------

# [Shadowrocket 懒人配置](#shadowrocket-懒人配置)

> [!NOTE]
>
> 懒人配置顾名思义是专为 `懒人` 打造的开箱即用[配置文件](#配置文件)，该系列配置包含两个文件：一个是 [基础配置](https://raw.githubusercontent.com/LOWERTOP/Shadowrocket/main/lazy.conf)，另一个在此基础上增加了 [代理分组/策略组](https://raw.githubusercontent.com/LOWERTOP/Shadowrocket/main/lazy_group.conf)。懒人配置不仅内置了详尽的注释文本，且经过精心调整内置设置以适应绝大多数用户的需求，也是 [官方群组](https://t.me/ShadowrocketApp) 除默认配置外首推的配置文件，适合各阶段用户使用

> 如需使用该系列配置文件，可复制下方相应地址 [添加配置](#配置文件) 或点击徽章一键安装
> 
> **懒人配置**
> >   ```
> >   https://raw.githubusercontent.com/LOWERTOP/Shadowrocket/main/lazy.conf
> >   ```
> > [![安装配置 懒人配置](https://img.shields.io/static/v1?label=安装配置&message=懒人配置&color=grey&logo=googledocs&logoColor=white&labelColor=blue&messageColor=white)](https://lowertop.github.io/Shadowrocket-First/redirect.html?url=shadowrocket://config/add/https://raw.githubusercontent.com/LOWERTOP/Shadowrocket/main/lazy.conf "一键安装本配置文件")
> 
> **懒人配置（含策略组）**
> >   ```
> >   https://raw.githubusercontent.com/LOWERTOP/Shadowrocket/main/lazy_group.conf
> >   ```
> > [![安装配置 懒人分流](https://img.shields.io/static/v1?label=安装配置&message=懒人分流&color=grey&logo=googledocs&logoColor=white&labelColor=blue&messageColor=white)](https://lowertop.github.io/Shadowrocket-First/redirect.html?url=shadowrocket://config/add/https://raw.githubusercontent.com/LOWERTOP/Shadowrocket/main/lazy_group.conf "一键安装本配置文件")

------

# [Shadowrocket 使用手册](#shadowrocket-使用手册)

> [!NOTE]
> 
> Shadowrocket（常被用户称为“小火箭”）是一款专为 iOS 设备设计的网络代理工具，同时也支持 Apple TV 和 Mac 设备（M系列芯片）。Shadowrocket 提供了灵活的配置选项，它通过将设备的网络流量转发至代理服务器，帮助用户绕过特定网络环境、访问被限制的内容，并提升在线隐私保护，满足不同用户的需求

> [!TIP]
> 
> **快速使用方法**
> 
> > * 首页 - 添加节点
> > * 设置 - 延迟测试方法，选择 `CONNECT`
> > * 首页 - 连通性测试，选择可用节点连接
> 
> 首次启动会提示 `安装VPN配置文件`，请点击 `好` 和 `允许` 才能正常使用

## [使用目录](#使用目录)
> [!TIP]
> * 点击目录标题可以快速定位到相关正文
> * 点击正文的蓝色标题可以快速回到目录

> * [首页](#软件首页)
>     * [添加节点](#添加节点)
>     * [添加WireGuard节点](#添加wireguard节点)
>     * [更新订阅节点](#更新订阅节点)
>     * [节点排序](#节点排序)
>     * [节点分享与整理](#节点分享与整理)
>     * [订阅节点筛选](#订阅节点筛选)
>     * [代理通过/代理链](#代理通过代理链)
>     * [全局路由区别](#全局路由区别)
>     * [连通性测试](#连通性测试)
>     * [修改测试地址](#修改测试地址)
>     * [场景](#场景)
>     * [简单模式](#简单模式)
>     * [启用回退](#启用回退)
> * [配置](#配置页面)
>     * [配置文件](#配置文件)
>     * [使用配置](#使用配置)
>     * [编辑配置](#编辑配置)
>     * [编辑纯文本](#编辑纯文本)
>     * [预览配置](#预览配置)
>     * [更新配置](#更新配置)
>     * [重新命名](#重新命名)
>     * [导出配置](#导出配置)
>     * [扩展配置](#扩展配置)
>     * [通用参数](#通用参数)💡
>     * [添加规则](#添加规则)
>     * [规则优先级](#规则优先级)
>     * [规则类型](#规则类型)
>     * [规则策略](#规则策略)
>     * [APP分流](#app分流)
>     * [更新规则集](#更新规则集)
>     * [预览规则集](#预览规则集)
>     * [修改DNS](#修改dns)
>     * [DNS-over-PROXY](#dns-over-proxy)
>     * [no-resolve的作用](#no-resolve的作用)
>     * [代理分组/策略组](#代理分组策略组)
>     * [代理分组类型](#代理分组类型)
>     * [脚本URL](#脚本url)
>     * [规则集URL](#规则集url)
>     * [复制配置文件](#复制配置文件)
>     * [Hosts](#hosts)
>     * [URL重写](#url重写)
>     * [HTTPS解密](#https解密)
>     * [负载均衡](#负载均衡)
>     * [模块](#模块)
>     * [证书模块](#证书模块)
>     * [身份证书密码](#身份证书密码)
> * [数据](#数据页面)
>     * [代理日志](#代理日志)
>     * [DNS日志](#dns日志)
>     * [iCloud自动同步](#icloud自动同步)
>     * [节点数据管理](#节点数据管理)
>     * [流量统计信息](#流量统计信息)
> * [设置](#设置页面)
>     * [延迟测试方法](#延迟测试方法)
>     * [小组件](#小组件)
>     * [按需求连接](#按需求连接)
>     * [隧道](#隧道)
>     * [前置代理](#前置代理)
>     * [代理共享](#代理共享)
>     * [检测代理](#检测代理)
>     * [代理类型](#代理类型)
>     * [开启UDP转发](#开启udp转发)
>     * [隐藏VPN图标](#隐藏vpn图标)
>     * [GEOIP数据库](#geoip数据库)
>     * [自动更新](#自动更新)
> * [其他](#其他问题)
>     * [自动切换节点](#自动切换节点)
>     * [SSL错误](#ssl错误)
>     * [节点旗帜](#节点旗帜)
>     * [节点感叹号](#节点感叹号)
>     * [微信转圈](#微信转圈)
>     * [模块消失](#模块消失)
>     * [VPN自动断开](#vpn自动断开)
>     * [定位权限](#定位权限)
>     * [编译原因](#编译原因)
>     * [下载Shadowrocket](#下载shadowrocket)
>     * [URL-Schemes](#url-schemes)

------

## [软件首页](#软件首页)

### [添加节点](#使用目录)

> * 首页 - 左上角 - 扫码添加
>   
> * 复制节点链接，如 `trojan://*` `vmess://*` `vless://*` 等，打开 Shadowrocket 时会自动识别导入
>   
>   `须开启剪贴板读取权限`
> 
> * 首页 - 右上角 `➕` - 类型 `Subscribe` - URL 栏输入服务器订阅链接 - 保存
> 
>   `订阅链接后面加上 "#1"、"#2"、"#3" 等，可以重复添加同一个订阅`
> 
> * 首页 - 右上角 `➕`，选择对应节点类型，填写节点配置信息并保存
> 
>   **Shadowrocket 已支持的协议类型**：`Shadowsocks、ShadowsocksR、Subscribe（订阅）、Vmess、VLESS、Relay、Socks5、Socks5 Over TLS、HTTP、HTTPS、HTTP2、Trojan、Hysteria、Hysteria2、TUIC、Juicity、WireGuard、Snell v2、Brook、Lua`

### [添加WireGuard节点](#使用目录)

> * 首页 - 右上角 `➕` - 类型选择 `WireGuard`，填写配置信息
> 
> * 复制如下格式的 `WireGuard` 配置信息，打开 Shadowrocket 时会自动弹出 `添加对话框`，点击添加
>   
>   ```
>   [Interface]
>   PrivateKey = xxxxxx
>   Address = 172.16.0.2/32
>   DNS = 1.1.1.1
>   MTU = 1420
>   [Peer]
>   PublicKey = xxxxxx
>   AllowedIPs = 0.0.0.0/0
>   AllowedIPs = ::/0
>   Endpoint = engage.cloudflareclient.com:2408
>   Reserved = 12,34,56
>   ```
>   如果没有自动弹出对话框，可能是因为设置中的 `允许检测剪贴板` 被关闭了，您可以重新打开，或者点击首页 `连通性测试` 下方的 `粘贴` 按钮，手动添加配置信息

### [更新订阅节点](#使用目录)

> * 订阅右滑 - 更新
> 
> * 点击首页的更新订阅按钮🔄
> 
> * 设置 - 订阅 - 打开时更新（刷掉后台，重新打开应用程序时会自动更新订阅）
> 
> * 设置 - 订阅 - 自动后台更新（需在系统 `设置`-`通用`-`后台App刷新` 中开启对 Shadowrocket 的允许，更新周期可设1-24小时）
> 
> * Shadowrocket 提供了 `更新订阅` 的快捷指令，可以实现自动化操作
> 
> * 长按屏幕的应用图标 - 更新订阅
>   
> ```
> 添加/更新订阅时异常的原因：
> forbidden 表示订阅被重置或令牌 token 错误
> not found 表示路径信息错误
> service unavailable 表示域名信息错误或域名被运营商屏蔽
> ```

### [节点排序](#使用目录)

> 设置 - 订阅 - 根据 `Ping` 排序

### [节点分享与整理](#使用目录)

> **节点分享**
> 
> > * 长按节点 - 拷贝，可以把节点链接分享给其他设备
> > 
> > * 左滑节点 - 二维码，其他设备可以通过扫码添加节点（二维码页面点击右上角的 `分享` 按钮，可以选择其他形式传送二维码）
> > 
> >   `节点二维码缺乏统一标准。某些协议 Vmess 的节点，当使用其他代理工具扫码添加时，可能会丢失部分节点信息，导致不能连接。如果遇到此问题，请仔细检查同一个节点的各项配置信息是否一致`
> > 
> > * 点击节点后面 `ⓘ`，滑动至页面底部，有多种分享节点的菜单
> > 
> > * 展开节点列表，点击连通性测试下方的编辑按钮 `•••`，勾选需要分享的节点，点击左上角的 `复制`，可以把多个节点链接同时分享给其他设备
> 
> **节点整理**
> 
> > * **调整顺序**：点击编辑按钮 `•••`，按住订阅后面的 `≡`图标可以调整订阅之间的上下顺序（本地节点默认置顶位置）
> > 
> > * **节点分类**：非订阅形式添加的节点，默认会归类为 `本地节点`。如果需要重新对本地节点进行分类，可以使用 `折叠` 功能。点击编辑按钮 `•••`，勾选节点，点击左上角的 `折叠`，为新分类的节点组命名（`折叠` 功能可以选择本地节点或者订阅节点）
> > 
> > * **删除节点**：点击编辑按钮 `•••`，点击左上角的 `删除`，可以选择删除全部节点或者删除连通性测试结果中的超时节点
> > 
> > * **滑动菜单**：向右滑动订阅，可以选择 `测试` 当前订阅节点的连通性，或者 `更新` 当前订阅节点。向右滑动节点，点击 `测试` 可以获取单个节点的连通性测试结果，点击 `复制`，可以在当前节点列表中新增一个同样配置信息的节点

### [订阅节点筛选](#使用目录)

> **节点筛选**
> 
> > 首页 - 订阅后面 `ⓘ` - 过滤
> > 
> > `分组、代理分组的正则写法与以下命令相同，但需删除前后 "/" 符号`
> > 
> > * 保留节点名称含有关键词 A 和 B 的节点：
> >   ```
> >   /(?=.*(A))^(?=.*(B))^.*$/
> >   ```
> > * 保留节点名称含有关键词 A 或 B 的节点：
> >   ```
> >   A|B
> >   ```
> > * 排除节点名称含有关键词 A 或 B 的节点：
> >   ```
> >   /^((?!(A|B)).)*$/
> >   ```
> > * 保留节点名称含有关键词 A 并排除含有关键词 B 的节点：
> >   ```
> >   /(?=.*(A))^((?!(B)).)*$/
> >   ```
> 
> **批量整理**
> 
> > 节点订阅筛选功能支持使用脚本代码批量整理和修改相应订阅中节点的功能选项及节点名称
> > 
> > * 批量给节点中的关键词 a 替换成 b：
> >   ```
> >   $server.title=$server.title.replace(/关键词a/g,'关键词b')
> >   ```
> > * 批量给节点名称增加 abc 开头的关键词：
> >   ```
> >   $server.title='abc'+$server.title
> >   ```
> > * 批量开启全部节点的片段：
> >   ```
> >   $server.reserved="1,40-60,30-50"
> >   ```
> > * 批量开启全部节点的多路复用：
> >   ```
> >   $server.mux=1
> >   ```
> > * 批量设置全部订阅节点的 代理链/链式代理/代理通过
> >   ```
> >   $server.chain="订阅名称/节点名称"
> >   ```
> >   ```
> >   $server['dialer-proxy']="UUID值"
> >   ```
> >   `第一种为正式命令，第二种为临时命令，过度期内两种方式以生效者为准。其中”UUID 值”可在中转节点或订阅的 JSON 文本中复制，第一种命令的“订阅名称/节点名称”也可以使用 UUID 值`
> 
> **其他命令**
> 
> > 该功能也支持更复杂的脚本指令，可以参阅 [此处示例](https://github.com/LOWERTOP/Shadowrocket-First#%E7%AD%9B%E9%80%89%E8%AE%A2%E9%98%85%E8%84%9A%E6%9C%AC)

### [代理通过/代理链](#使用目录)

> 当前代理通过另一个代理进行连接，支持多级链式代理。使用代理链方法：
> 
> * 使用节点 A 连接，点击节点 A 后面 `ⓘ`，`代理通过` 选择节点 B，流量走向：`Client` - `B` - `A` - `Web server`
> * 支持使用整个订阅作为中转代理链，其生效节点是在该订阅的节点中随机选择。具体生效节点可在 VPN 日志搜索 `backend chain` 确认
> * 支持批量修改订阅节点代理链，实现同时部署多个节点的代理链。具体命令可查看 [订阅节点筛选 - 批量整理](#订阅节点筛选) 中的相关指令

### [全局路由区别](#使用目录)

> * **配置**：流量根据设定规则进行分配，有些通过节点连接，有些则不通过
> * **代理**：全部流量都通过同一个节点连接
> * **直连**：全部流量都不通过节点连接
> * **场景**：根据不同的网络连接类型（Wi-Fi、蜂窝数据）自动切换到预先设置的路由模式，并选择对应的配置文件和节点连接

### [连通性测试](#使用目录)

> 点击首页的 `连通性测试`，节点列表将会显示以毫秒（ms）为单位的延迟数字，这是数据包的传输时间，不同的 `延迟测试方法` 对应不同的计算结果。长按首页的 `连通性测试`，可以临时调整测试方法，仅对本次测试生效
> 
> 设置 - 延迟测试方法
> 
> * **TCP**：建立 `TCP` 连接的往返时间
> * **ICMP**：发送 `ICMP` 回显请求报文和接收 `ICMP` 回显应答报文的往返时间
> * **CONNECT**：向测试 URL 发送一个 `HTTP HEAD` 请求，测量从发送请求到接收响应头部信息的往返时间
> 
>   `请优先选择 CONNECT，因为它更能准确反映节点的连通性`
> 
> 延迟大小与网络上传下载速度没有直接关系，测速请使用其他方法，如：
> <https://www.speedtest.net>

### [修改测试地址](#使用目录)

> **用于首页和分组节点的延迟测试**
> 
> > * 首页 - 全局路由 - 分组 - URL 测试设置
> 
> **用于代理分组节点的延迟测试**
> 
> > * 点击配置文件 `ⓘ` - 代理分组 - 右上角 `➕` - 最下方URL栏

### [场景](#使用目录)

> 场景是根据不同的网络连接类型（Wi-Fi、蜂窝数据）自动切换到预先设置的路由模式，并选择对应的配置文件和节点连接
> > * 首页 - 全局路由 - 设置的 `场景` - 添加场景
> > * 为指定的网络连接类型设置对应的路由模式（`配置` `直连` `代理`），类型（`节点` `分组`）、配置文件 及 备注
> > * 网络连接类型分别为：Wi-Fi、蜂窝数据、默认。选择Wi-Fi类型时，SSID需填写Wi-Fi名称
> > * 首页 - 全局路由 - 选择 `场景`
>
> 软件支持添加蜂窝数据场景，支持以 `网络接口` 作为匹配条件
> > * 默认（留空）代表接口 `pdp_ip0`
> > * 当设备启用了多个蜂窝数据网络时，可在 Shadowrocket 的 设置 > 诊断 > 网络 中查看对应的接口信息
> > * 输入格式：`pdp_ip1` `pdp_ip2` `pdp_ip3` 等
> 
> 首次添加场景，可能会弹出申请权限的对话框，具体原因请看 [定位权限](#定位权限)。当没有允许定位权限时，场景列表的☑️标记不会随着网络类型的切换而自动切换，但这不影响场景功能的正常生效
> 
> 设置 - 隧道/按需求连接 中的 `包含所有网络` 相关选项可能会对场景模式的生效造成影响


### [简单模式](#使用目录)

> 简单模式是一种以相对简单的方式实现自动测试并选择延迟低的节点进行连接的设置模式
> 
> * 首页 - 全局路由 - 分组 - 简单模式

> **节点的范围是什么？**
> > 当开启简单模式，此时下方会出现分组选项，如果没有继续添加分组的操作，节点范围就是首页全部节点，如果添加分组，范围就变成分组里的节点
> 
> **自动测试的周期是多久？延迟低的判断依据是什么？**
> > `首页` - `全局路由` - `分组` - `URL测试设置`，这里规定了测试的间隔时间，默认 600s，即表示每 10 分钟自动进行一次节点延迟测试。相邻两次测试结果中最小延迟值的对比，根据公差机制决定是否切换节点，公差越大，触发节点切换的频次越低，默认 0ms，即表示只要后面测试结果的最低延迟节点比前面测试结果的最低延迟节点延迟小就会自动切换
> 
> **切换的节点给什么规则使用？**
> > Shadowrocket 内置策略 `proxy`，简单模式时自动切换的节点使用于所有指向 `proxy` 策略的规则
> 
> **简单模式是自动切换延迟低节点，代理分组的 url-test 类型也是自动切换延迟低节点，两者有何不同？**
> > 代理分组创建后，需要在规则中修改策略指向，而简单模式已经关联 `proxy` 策略，节省了修改规则的步骤<br>
> > `全局路由` 选择 `代理` 时将导致所有 `代理分组` 失效，而简单模式依然能够实现自动切换节点
> 
> **添加分组时，`测速` 开关是什么作用？**
> > 开启测速，这个分组才允许自动切换节点。不开启测速，这个分组只能手动选择节点

### [启用回退](#使用目录)

> 首页 - 全局路由 - 启用回退
> 
> `启用回退` 的功能是当节点连接失败时自动切换其他可用节点
> * 连接失败3次才会触发回退机制
> * 节点只满足可用性，不要求是最低延迟节点
> * 随机切换，不按照节点顺序选择
> * 策略为 `proxy`，节点切换范围就是首页全部节点，如果开启简单模式并选择分组，则范围缩小至分组内节点
> * 策略为分组/代理分组，节点切换范围就是分组或代理分组内节点
> * 具体切换到哪个节点，请查看 [代理日志](#代理日志)

------

## [配置页面](#配置页面)

### [配置文件](#使用目录)

> Shadowrocket 的配置文件（通常以 .conf 格式存在）主要用于快速设置和软件的主要功能，简化用户手动配置的流程。配置文件还可以在多设备间同步以及分享配置文件给其他用户，以快速部署相同设置<br>
> Shadowrocket 内置了一个默认配置文件 `default.conf`，其中包含了国内外主要网站或服务的分流规则，一般可以满足大多数用户的基本需求。此配置文件的内容跟随应用更新而做不定期的调整。如果在使用过程中错误修改或误删配置文件，可以点击 `配置` - `恢复默认配置`。
> 
> 添加配置文件方法：
> > * 从 URL 下载配置
> >   * 配置 - 右上角 `➕` - 粘贴配置链接 - 下载 - 点击对应的配置文件 - 使用配置
> >   * Shadowrocket兼容使用 `Clash YAML格式` 的配置文件。使用含节点信息的标准 Clash 链接可以同时导入配置文件和节点信息
> >  
> > * 从本地存储或云盘导入
> >   * 配置 - 从云导入，点击对应存储路径的配置文件
> 
> 点击配置文件，显示操作菜单：
> > * [使用配置](#使用配置)
> > * [编辑配置](#编辑配置)
> > * [编辑纯文本](#编辑纯文本)
> > * [预览配置](#预览配置)
> > * [更新配置](#更新配置)
> > * [扩展配置](#扩展配置)
> > * [重新命名](#重新命名)
> > * [导出配置](#导出配置)
> 
> 点击配置文件的 `ⓘ` 图标，进入编辑菜单：
> > * [通用](#通用参数)
> > * [规则](#添加规则)
> > * [Hosts](#hosts)
> > * [URL重写](#url重写)
> > * [HTTPS解密](#https解密)
> > * 脚本
> > * [代理分组](#代理分组策略组)
> > * [脚本URL](#脚本url)
> > * [规则集URL](#规则集url)
> > * [复制](#复制配置文件)
> > * 替换策略
> > * 测试规则

### [使用配置](#使用目录)

> 点击 `使用配置` 可以启用该配置文件。 `使用配置` 可以对该配置文件包含的远程规则集、脚本等远程资源进行更新

### [编辑配置](#使用目录)

> 使用UI交互界面对配置文件的可设置项进行调整

### [编辑纯文本](#使用目录)

> 使用纯文本模式对配置文件的可设置项进行调整
> 
> 配置文件的纯文本编写方法，请参考：
> * [懒人配置](https://raw.githubusercontent.com/LOWERTOP/Shadowrocket/main/lazy.conf)<br>
> * [懒人配置（含策略组）](https://raw.githubusercontent.com/LOWERTOP/Shadowrocket/main/lazy_group.conf)

### [预览配置](#使用目录)

> 查看配置文件的纯文本格式

### [更新配置](#使用目录)

> 更新当前配置文件以及当前所用的规则集、脚本等远程资源。该选项仅当配置文件是以远程配置文件的形式添加进来的才会出现。软件同时提供自动更新功能，详细更新设置技巧请参见 [自动更新](#自动更新) 词条

### [重新命名](#使用目录)

> 重命名当前配置文件

### [导出配置](#使用目录)

> 将当前配置文件以文件的形式导出

### [扩展配置](#使用目录)

> * 从配置 a 扩展出配置 b，此时默认关系是 b 包含 a，也可以理解为 b 继承了 a 的内容
> 
> * 配置 b 优先级高于配置 a，该功能是对配置建立包含关系，以满足同时使用多个配置的需求
> 
> * 点击配置文件 `ⓘ` - 通用 - 包含配置，可以修改或解除包含关系

### [通用参数](#使用目录)

> **旁路系统（bypass-system）**：如果禁用此选项，可能会导致一些系统问题，如推送通知延迟
> 
> **跳过代理（skip-proxy）**：此选项强制域名或IP的连接范围由 Shadowrocket `TUN 接口` 来处理，而不是 Shadowrocket 代理服务器。此选项用于解决一些应用程序的一些兼容性问题
> 
> **TUN旁路路由（tun-excluded-routes）**：Shadowrocket `TUN接口`只能处理 `TCP 协议`。使用此选项可以绕过指定的IP范围，让其他协议通过
> 
> **DNS覆写（dns-server）**：使用普通 DNS 或加密 DNS（如 `doh` `doq` `dot` 等）覆盖默认的系统 DNS。有些 `dns over https` 支持 `http3`，所以尝试查询，如果支持就切换到 `http3`，可在 `doh链接` 后面加上 `#no-h3` 关闭。`doh` 强制通过 `h3` 查询的写法是将 `https` 改成 `h3`，如`h3://dns.alidns.com/dns-query`
> 
> **备用DNS（fallback-dns-server）**：当覆写 DNS 查询失败或查询时间超过2秒，Shadowrocket 会自动回退备用 DNS。如需指定多个 DNS，可用逗号分隔。`system` 表示回退到系统 DNS
> 
> **启用IPv6支持（ipv6）**：`false` 表示不启用，`true` 表示启用。即使不启用此选项，当本地网络环境支持 IPv6，并且节点域名支持 IPv6 解析，Shadowrocket 也会使用节点的 IPv6 地址进行访问。解决方法是关闭节点域名的 IPv6 解析，或者在配置文件的 `[Host]` 项目下为节点域名指定 IP 地址
> 
> **首选IPv6（prefer-ipv6）**：优先向 IPv6 的 DNS 服务器查询 `AAAA` 记录，优先使用 `AAAA` 记录。`false` 表示不启用
> 
> **私有IP应答（private-ip-answer）**：如果不启用该选项，域名解析返回私有 IP，Shadowrocket 会认为该域名被劫持而强制使用代理
> 
> **TUN包含路由（tun-included-routes）**：默认情况下，Shadowrocket 接口会声明自己为默认路由，但由于 Wi-Fi 接口的路由较小，有些流量可能不会通过 Shadowrocket 接口。使用此选项可以添加一个较小的路由表
> 
> **总是真实IP（always-real-ip）**：这个选项要求 Shadowrocket 在 `TUN` 处理 DNS 请求时返回一个真实的 IP 地址而不是假的IP地址
> 
> **DNS劫持（hijack-dns）**：有些设备或软件总是使用硬编码的 DNS 服务器，例如 Netflix 通过 Google DNS（`8.8.8.8` 或 `8.8.4.4`）发送请求，您可以使用此选项来劫持查询
> 
> **包含配置（include）**：表示当前配置包含另一个配置的内容，当前配置的优先级高于被包含配置。该选项是对配置建立包含关系，以满足同时使用多个配置的需求
> 
> 💡 **dns-direct-system**：直连的域名类规则使用系统 DNS 进行查询。`false` 表示不启用
> 
> 💡 **icmp-auto-reply**：ping 数据包自动回复
> 
> 💡 **always-reject-url-rewrite**：不开启时，「重写的REJECT策略」默认只有在配置模式下生效。开启后，可以令该策略在其他全局路由模式下都生效
> 
> 💡 **dns-direct-fallback-proxy**：直连域名解析失败后使用代理。`false` 表示不启用
> 
> 💡 **udp-policy-not-supported-behaviour**：当 UDP 流量匹配到规则里不支持 UDP 转发的节点策略时重新选择回退行为，可选行为包括 `DIRECT` `REJECT`。`DIRECT` 表示直连转发 UDP 流量，`REJECT` 表示拒绝转发 UDP 流量
>
> 💡 **stun-response-ip**：此选项包含两个命令：`stun-response-ip` 和 `stun-response-ipv6`。该选项允许返回一个虚假的IP地址，如 `stun-response-ip=1.1.1.1`  `stun-response-ipv6=::1`，目的是防止真实IP地址泄漏，提高 WebRTC 的隐私和安全性
>
> 💡 **compatibility-mode**：网络兼容模式。`0 - 禁用`；`1 - Proxy with Loopback Address`；`2 - Proxy Only`；`3 - TUN Only`。当参数的值设定为3时的效果等同于：设置 - 代理 - 代理类型 - None
>
> 💡 **always-ip-address**：强制所有域名使用本地 DNS 解析。设置为 `true` 表示启用。（此参数为隐藏属性，建议谨慎设置，可能导致相关域名的 CDN 失效。）
> 
> `带💡符号的参数只能通过配置文件的纯文本模式进行设置，没有 UI 操作选项`

### [添加规则](#使用目录)

> 在 Shadowrocket 中，"规则"是指用来决定哪些网络请求应该走代理、哪些请求应该直接连接互联网的规则集合。规则通常是基于用户的需求来配置 [规则策略](#规则策略)，目的是实现对流量的精细控制
> 
> * 点击配置文件 `ⓘ` - 规则 - 右上角 `➕`，根据需求选择 [规则类型](#规则类型) 和 [规则策略](#规则策略)，填写规则内容
> 
> * 数据 - 代理 - 启用日志记录，产生网络活动后回到该页面，从最近的日志中查看网络活动记录，点击任一记录查看详情，点击右上角`•••`选择类型添加规则
> 
> * 规则匹配需要着重注意 [规则的优先级](#规则优先级) 顺序

### [规则优先级](#使用目录)

> 规则的匹配是从上到下逐条匹配的，一旦匹配到某条规则，Shadowrocket 就会停止继续匹配。因此，规则的顺序非常重要，优先级高的规则应该放在前面
>
>   * 上面的规则优先于下面的规则
>   * 域名类的规则优先于IP类规则
>   * 模块中的规则优先于配置文件

### [规则类型](#使用目录)

> **DOMAIN-SUFFIX**：匹配请求域名的后缀
> 
> > 如 `DOMAIN-SUFFIX,example.com,DIRECT` 可以匹配到 `a.example.com` `a.b.example.com`
> 
> **DOMAIN-KEYWORD**：匹配请求域名的关键词
> 
> > 如 `DOMAIN-KEYWORD,exa,DIRECT` 可以匹配到 `a.example.com` `a.b.example.com`
> 
> **DOMAIN**：匹配请求的完整域名
> 
> > 如 `DOMAIN,www.example.com,DIRECT` 只能匹配到 `www.example.com`
> 
> **USER-AGENT**：匹配用户代理字符串，支持使用通配符`*`
> 
> > 如 `USER-AGENT,MicroMessenger*,DIRECT` 可以匹配到 `MicroMessenger Client`
> 
> **URL-REGEX**：匹配 URL 正则式
> 
> > 如 `URL-REGEX,^https?://.+/item.+,REJECT` 可以匹配到 `https://www.example.com/item/abc/123`
> 
> **IP-CIDR**：匹配 IPv4 或 IPv6 地址
> 
> > 如 `IP-CIDR,192.168.1.0/24,DIRECT` 可以匹配到IP段 `192.168.1.1～192.168.1.254`。当域名请求遇到IP类规则时，Shadowrocket会向本地DNS服务器发送查询请求，以判断主机IP是否匹配规则。若IP类规则加 `no-resolve`（如：`IP-CIDR,172.16.0.0/12,DIRECT,no-resolve`），则域名请求将会跳过此规则，不会触发本地DNS查询
> 
> **IP-ASN**：匹配 IP 地址隶属的 ASN 编号
> 
> > 如 `IP-ASN,56040,DIRECT` 可以匹配到属于China Mobile Communications Corporation网络的IP地址
> 
> **RULE-SET**：匹配规则集内容。规则集的组成部分需包含规则类型
> 
> **DOMAIN-SET**：匹配域名集内容。域名集的组成部分不包含规则类型
> 
> **SCRIPT**：匹配脚本名称
> 
> **DST-PORT**：匹配目标主机名的端口号
> 
> > 如 `DST-PORT,443,DIRECT` 可以匹配到 443 目标端口
>   
> **GEOIP**：匹配 IP 数据库
> 
> > 如 `GEOIP,CN,DIRECT` 可以匹配到归属地为CN的IP地址
> 
> **FINAL**：兜底策略
> 
> > 如 `FINAL,PROXY` 表示当其他所有规则都匹配不到时才使用 `FINAL` 规则的策略
> 
> **AND**：逻辑规则，与规则
> 
> > 如 `AND,((DOMAIN,www.example.com),(DST-PORT,123)),DIRECT` 可以匹配到 `www.example.com:123`
> 
> **NOT**：逻辑规则，非规则
> 
> > 如 `NOT,((DST-PORT,123)),DIRECT` 可以匹配到除了 `123` 端口的其他所有请求
> 
> **OR**：逻辑规则，或规则
> 
> > 如 `OR,((DST-PORT,123),(DST-PORT,456)),DIRECT` 可以匹配到 `123` 或 `456` 端口的所有请求
> 
> **PROTOCOL**：匹配传输协议类型
> 
> > `PROTOCOL` 类型不支持单独使用，只能作为子规则类型嵌套于逻辑规则当中。如 `AND,((PROTOCOL,UDP),(DST-PORT,443)),REJECT-NO-DROP`

### [规则策略](#使用目录)

> **PROXY**：代理。通过代理服务器转发流量
> 
> **DIRECT**：直连。连接不经过任何代理服务器
> 
> **REJECT**：拒绝。返回 HTTP 状态码 404，没有内容
> 
> **REJECT-DICT**：拒绝。返回 HTTP 状态码 200，内容为空的JSON对象
> 
> **REJECT-ARRAY**：拒绝。返回 HTTP 状态码 200，内容为空的JSON数组
> 
> **REJECT-200**：拒绝。返回 HTTP 状态码 200，没有内容
> 
> **REJECT-IMG**：拒绝。返回 HTTP 状态码 200，内容为 1 像素 GIF
> 
> **REJECT-TINYGIF**：拒绝。返回HTTP状态码200，内容为 1 像素 GIF
> 
> **REJECT-DROP**：拒绝。丢弃 IP 包
> 
> **REJECT-NO-DROP**：拒绝。返回 ICMP 端口不可达
> 
> 除此之外，规则策略还可以选择 `代理分组` `订阅名称` `分组` `服务器节点`

### [APP分流](#使用目录)

> 根据不同 App 或特定服务指定分流规则，并使其按照设定的规则执行代理策略
> 
> 示例：YouTube App 分流走代理
> 
> * 复制 YouTube 的规则集链接
>   ```
>   https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/YouTube/YouTube.list
>   ```
> * 点击配置文件 `ⓘ` - 规则 - 右上角 `➕`，类型选择 `RULE-SET`，策略选择 `PROXY`，输入框内粘贴 `规则集链接`，保存完成（策略可以根据需求使用其他选项）
> 
> iOS系统没有常规分应用代理的操作，只能通过 `域名` / `ip` / `ua` 规则实现app分流效果。可自行抓包，或者订阅 [blackmatrix7](https://github.com/blackmatrix7) 的 [规则集](https://github.com/blackmatrix7/ios_rule_script/tree/master/rule/Shadowrocket)。如果引用的链接是域名集，添加规则时，类型请选择 `DOMAIN-SET`

### [更新规则集](#使用目录)

> * 手动更新：点击配置文件 - 使用配置
> * 自动更新：[自动更新](#自动更新)

### [预览规则集](#使用目录)

> 点击配置文件 - 编辑配置 - 规则 - 在规则集上左滑 - 预览

### [修改DNS](#使用目录)

> * 点击配置文件 `ⓘ` - 通用 - DNS 覆写，删除 `system`，添加 `223.5.5.5,119.29.29.29`。也可以使用 [通过代理使用DNS](#dns-over-proxy) 以及加密DNS，如 `DNS-over-TLS` `DNS-over-HTTPS` `DNS-over-QUIC`
> 
> * **备用DNS**：当覆写的 DNS 查询失败后回退备用 DNS 进行查询。如需指定多个 DNS，可用逗号分隔。`system` 表示回退到系统 DNS

### [DNS-over-PROXY](#使用目录)

> 通过代理连接 DNS 服务器
>
> * **proxy=name**
> 
> > 需要注意此处的代理名称仅支持 http 编码<br>
> > 以 `香港 01` 示例：
> > ```
> > dns-server=https://dns.google/dns-query#proxy=%E9%A6%99%E6%B8%AF%2001
> > ```
> 
> * **ecs=子网范围**
> 
> > ecs 参数用于设置 EDNS Client Subnet (ECS)，向 DNS 服务器传递客户端的子网信息。ECS 允许 DNS 服务器根据指定的子网范围（而非实际客户端 IP）来返回最优结果
> 
> * **ecs-override=true**
> 
> > ecs 参数的强制覆盖。即使客户端的实际 IP 提供了不同的地理位置，查询会强制使用 ecs 指定的子网范围
> > 
> > 示例：
> > ```
> > dns-server=https://dns.google/dns-query#ecs=120.76.0.0/14|2620:149:af0::10/56&ecs-override=true
> > ```
> > ```
> > dns-server=https://dns.google/dns-query#proxy=name&ecs=1.1.0.0/14|2620:149:af0::10/56&ecs-override=true
> > ```

### [no-resolve的作用](#使用目录)

> * 当域名请求遇到 IP 类规则时，Shadowrocket 会向本地DNS服务器发送查询请求，以判断主机 IP 是否匹配规则
> 
> * 若IP类规则加 `no-resolve`，则域名请求将会跳过此规则，不触发本地 DNS 查询。如：
>   ```
>   IP-CIDR,172.16.0.0/12,DIRECT,no-resolve
>   ```

### [代理分组/策略组](#使用目录)

> * 点击配置文件 `ⓘ` - 代理分组 - 右上角 `➕`。填写名称，根据需求选择类型，通过 `正则` 匹配策略，或者从策略输入框后面的 `•••` 手动添加策略，保存
> 
> * 策略是规则的组成部分，创建的代理分组只有放到规则里才能发挥作用
>   * 进入对应规则的详情页，点击策略选项，从列表中选择所需的代理分组，保存
> 
> * 首页下拉，可以快捷进入代理分组界面

### [代理分组类型](#使用目录)

> **select**：手动指定所用代理
> 
> **url-test**：根据设定的自动测试周期和结果自动切换延迟最低节点
> 
> **fallback**：节点不可用时自动切换其他可用节点，其所使用的可用节点范围被上次自动测试结果所限
> 
> **load-balance**：不同规则的请求使用分组里的不同节点进行连接，相同的域名会使用同一个节点
> 
> **random**：随机使用分组里的不同节点进行连接，相同的域名可能使用不同的节点

### [脚本URL](#使用目录)

> 配置 -配置文件 - 编辑配置 - 脚本 URL
> 
> 当前使用的所有脚本的展示页面，`√` 表示当前脚本状态生效，`×` 表示当前脚本状态失效，点击脚本地址可重新拉取并弹出状态提示

### [规则集URL](#使用目录)

> 配置 -配置文件 - 编辑配置 - 规则集URL
> 
> 当前使用的所有规则集的展示页面，`√` 表示当前规则集状态生效，`×` 表示当前规则集状态失效，点击规则集地址可重新拉取并弹出状态提示

### [复制配置文件](#使用目录)

> 配置 - 点击配置文件 - 编辑配置 - 复制
> 点击该选项可将当前配置生成一份备份并命名为 `*-copy.conf`

### [Hosts](#使用目录)

> 主要功能
> > * 将特定域名映射到指定 IP 地址，绕过 DNS 解析，直接控制域名到 IP 的对应关系
> > * 将特定域名指定特定的 DNS 服务器进行解析
> 
> 常见用途
> 
> > * 屏蔽广告/追踪域名：将广告域名解析到无效 IP（如 0.0.0.0 或 127.0.0.1），使其无法加载
> > * 绕过 DNS 污染：强制将某些域名指向正确的 IP，避免被劫持
> > * 本地开发调试：将测试域名指向本地服务器 IP
> > * 加速访问：手动指定更快的 CDN IP

### [URL重写](#使用目录)

> 功能作用
> > * 修改 HTTP(S) 请求/响应，动态拦截并修改请求的 URL、头部或内容
> 
> 常见用途
> > * 去广告：将广告请求重定向到空地址或本地
> > * 反追踪：移除 URL 中的跟踪参数（如 utm_source）
> > * 路径修正：调整 API 请求路径以适配不同服务器
> > * 调试工具：将生产环境请求转发到测试服务器

### [HTTPS解密](#使用目录)

> 打开HTTPS解密方法：
> * 点击配置文件 `ⓘ` - HTTPS 解密 - 证书 - 生成新的 CA 证书 - 安装证书
> 
> * 系统设置 - 已下载描述文件 - 安装
> 
> * 系统设置 - 通用 - 关于本机 - 证书信任设置 - 开启对应 Shadowrocket 证书信任

### [负载均衡](#使用目录)

> 使用负载均衡策略类型方法：
> 
> 点击配置文件 `ⓘ` - 代理分组 - 右上角 `➕`，类型选择 `load-balance`
> 
> `load-balance` 表示不同规则的请求使用分组里的不同节点进行连接，相同的域名会使用同一个节点

### [模块](#使用目录)

> 模块是指为 Shadowrocket 提供额外功能的插件或者扩展项，一般是以增强或自定义软件的使用体验为出发点。模块的写法与配置文件相同，且模块的优先级高于配置文件，可以在模块里设置通用设置以及添加规则、Hosts、重写、脚本、证书内容、解密主机名等
>
> 模块 `[MITM]` 部分需要加 `%APPEND%`，表示把内容插入到配置中，不加时会覆盖配置中对应内容，并影响其他模块功能
> ```
> hostname = %APPEND% 主机名
> ```
> 
> **下载远程模块**
> > * 配置 - 模块 - 右上角 `➕` - 填写链接 - 下载
> 
> **本地新建模块**
> > * 配置 - 模块 - 新建模块 - 编辑后保存
> 
> **备注**
> > * 对正在使用的配置 [开启 HTTPS 解密](#https解密)，才能使包含 MITM 的模块完整生效，不包含 MITM 的模块除外
> > * 因模块可能包含不同规则，所以大多数模块仅在 [全局路由](#全局路由区别) 设为配置时生效，不包含规则类的模块除外
> > * iOS 15 之后，NE的内存限制由 15 MB 增加到了 50 MB，低版本系统可能因内存不足导致模块失效或 [VPN 自动断开](#vpn自动断开)

### [证书模块](#使用目录)

> 切换配置文件时免除重复安装 CA 证书方法：
> 
> * 点击「已安装证书的配置文件」后面 `ⓘ` - HTTPS 解密 - 证书后面 `ⓘ` - 复制
> 
> * 新建模块：
> 
>   软件 ` 配置 ` 页面 - ` 模块 ` - ` 新建模块 `，粘贴并自行修改以下内容：
>   
>   ```
>   #!name=证书（名字可更改）
>   [MITM]
>   enable=true
>   ca-passphrase=证书密码（即「已安装证书的配置文件」的证书密码，默认密码是Shadowrocket）
>   ca-p12=证书内容（即剪贴板复制的内容）
>   ```
>   原本是可以省略 `ca-passphrase` 这行参数。但由于引用的配置文件可能已经包含了证书密码，且证书密码可能不是 Shadowrocket，为防止出错，因此才增加 `ca-passphrase` 参数来覆盖引用的配置文件的证书密码
> 
>   `enable=true` 忽略当前配置文件内的HTTPS解密状态，使用该模块的证书进行HTTPS解密

### [身份证书密码](#使用目录)

> Shadowrocket 安装 CA 证书时，如果遇到「输入证书 `身份证书` 的密码」页面，可以尝试输入：Shadowrocket

------

## [数据页面](#数据页面)

### [代理日志](#使用目录)

> `代理日志` 记录了网络活动过程中 Shadowrocket 处理请求的具体信息
> * 数据 - 代理 - 启用日志记录
> 
> * 产生网络活动时，返回 `数据` - `代理` 页面查看日志文件
> 
> * 每条记录包含信息：
>     * 请求 URL
>     * 请求匹配的规则策略
>     * 请求传输协议
>     * 请求发送时间
> 
> * 记录显示 `MITM`，表示请求域名已启用解密
> 
> * 点击每条记录查看详情，详情页右上角 `•••` 可以选择类型添加规则
> 
> * `数据` - `代理` 页面，右上角 `•••` 可以手动删除所有日志文件。日志文件页面，右上角 `•••` 可以选择导出
> 
>   `数据 - 自动删除 - 打开，程序会自动删除7天前的日志文件。Shadowrocket 已连接状态，手动删除将保留最新的日志文件，未连接时，手动删除所有`

### [DNS日志](#使用目录)

> `DNS 日志` 记录了网络活动过程中 DNS 服务器处理域名查询请求的具体信息
> * 数据 - 代理 - DNS - 启用日志记录
> 
> * 产生网络活动时，返回 `数据` - `DNS` 页面查看日志文件
> 
> * 每条记录包含信息：
>     * 请求域名
>     * 查询结果
>     * DNS 响应时间
>     * 处理请求的 DNS
> 
> * 旗帜是根据返回IP地址的地理位置信息自动显示
> 
> * `覆写 DNS` 不可用或未返回有效响应时，回退 `备用 DNS` 来查询域名
> 
>   `记录信息中如果响应时间超过2秒，意味着系统正在触发回退机制`

### [iCloud自动同步](#使用目录)

> Shadowrocket 支持将服务器节点、配置文件、模块和脚本文件等数据类型自动同步至 iCloud 云端
> * 数据 - iCloud - 自动同步 - 打开
> 
> * 设备 `设置` - `账号` - `iCloud`，确保使用iCloud的APP列表中已经开启 Shadowrocket 和 `iCloud云盘` 项目，否则会出现 `iCloud自动同步失败` 的提示
> 
> * 同步成功时，点击 `iCloud文件` 可以看到存储云端的配置文件
> 
> * `文件app` - `iCloud云盘` - Shadowrocket，可以看到存储云端的所有数据。其中的 `shadowrocket.v2.model` 文件包含服务器节点的配置信息
> 
> * iCloud服务中断、网络连接问题以及其他复杂原因可能导致 iCloud 同步异常，这种情况建议选择手动删除iCloud备份并重新同步数据
> 
>   `如果用户删除首页某个节点后发现它又自动恢复，可以尝试以下解决方法：数据 - iCloud，服务器节点下面点击删除iCloud备份和同步服务器节点`
> 
> * 添加的 `场景` 和 `分组` 不属于 iCloud 自动同步的数据类型，需要手动备份下载，才能在设备间共享数据

### [节点数据管理](#使用目录)

> **导出节点**：将首页的所有节点数据整合成一个 JSON 文件，选择存储在本地或云端，也可以通过其他共享方式传输文件
> 
> **导入节点**：将存储在本地或云端 JSON 文件中的节点数据解析并添加到首页
> 
> **删除本地节点**：一键删除首页所有节点数据

### [流量统计信息](#使用目录)

> `统计` 是 Shadowrocket 开启连接后接管设备所有网络传输的流量统计信息
> * 数据 - 统计
> 
> * 统计包含信息：
>     * 开始时间
>     * 连接时间
>     * Wi-Fi 和蜂窝数据的上下行流量
>     * 流量分流的柱形图统计
> 
> * 默认记录所有流量统计信息。打开 `启用存档` 将会单独记录每一次连接的流量统计信息，关闭首页连接后可以从`归档`查看
> 
> * 点击右上角 `•••` 可以重置统计信息
> 
> 首页 `订阅` 支持显示流量统计信息。方法是在订阅链接指向的纯文本base64编码前添加 `STATUS=xxx` 或 `REMARKS=xxx` 字段，这样订阅名称下方就能显示自定义信息。如果没有添加字段或者隐藏用户代理字符串，可能导致不返回相关统计信息，只显示时间

------

## [设置页面](#设置页面)

### [延迟测试方法](#使用目录)

> 详见词条 [连通性测试](#连通性测试)

### [小组件](#使用目录)

> 设置 - 小组件
> > 
> > * **服务器节点**：根据需求添加6个常用节点，点击 `Today 小组件` 右上角的 `>` 可以展开查看，方便手动切换节点
> > 
> > * **显示Ping值**：启用后，长按 `Today小组件` 中心位置可以测试 `服务器节点` 连通性并显示延迟数字
> > 
> > * **根据Ping排序**：启用后，长按 `Today小组件` 中心位置可以测试 `服务器节点` 连通性并依延迟大小自动排序
> 
> 添加小组件方法：
> 
> Today 小组件
> 
> > * 负一屏 - 编辑 - 自定 - 点击 Shadowrocket 旁边的 `添加` 按钮  `➕`。（系统要求低于 iOS 18）
> 
> 屏幕小组件
> 
> > * 长按屏幕 - 左上角 `➕` - Shadowrocket，选择合适类型添加。（系统要求≥ iOS 17）
> 
> 更新 Shadowrocket 后，如果找不到小组件添加按钮，请尝试重启手机。如果小组件显示 `无法加载`，请尝试以下方法：
> 
> > * 系统设置 - 通用 - 语言与地区，添加或删除一种其他语言

### [按需求连接](#使用目录)

> **始终开启**
> > * VPN 保持连接状态。意外断开或者重启设备，也会自动连接
> > 
> > * 通过应用 `首页` 临时关闭连接。设备设置中的 VPN 状态以及小组件开关不能直接关闭
> > 
> > * `脚本`/`模块`/`解密` 等需求比较多时建议开启
> 
> **按需求连接**
> > * 根据添加的 `按需求规则` 自动切换 VPN 状态。默认规则是任意网络类型下保持连接状态，相当于 `始终开启`
> > 
> > * 按需求规则：
> >     * 当访问列表中的 `域名` 时，系统会向 Shadowrocket 发送请求，如果响应成功，VPN 自动连接
> >     * 网络中指定的 `DNS`（通常认为是网络运营商/Wi-Fi 路由器提供的 DNS 服务器地址）与列表任一内容相匹配时，VPN 自动连接或断开
> >     * `SSIDS` 填写需要匹配的 Wi-Fi 名称
> >     * VPN 连接行为可以通过 `网络类型`/`域名`/`DNS` 条件触发
> >     * VPN 断开行为不能通过 `域名` 条件触发
> >     * 从上到下依次匹配添加的 `按需求规则`
> > * 添加 `按需求规则` 后，打开 `按需求连接` 开关，规则才能生效
> > 
> > * 同时打开 `始终开启` 和 `按需求连接`，只有 `始终开启` 选项能够生效
>   
> **睡眠时断开**
> > * 当设备进入睡眠状态，VPN 自动断开连接
> > 
> > * Shadowrocket 响应系统发送的睡眠指令才会断开连接，有时候熄屏的系统未必处于睡眠状态
> 
> **显示断开信息**
> > * 显示 VPN 断开连接的通知信息

### [隧道](#使用目录)

> **强制路由**
> 
> > 如果开启，这个隧道的路由规则将优先于任何本地自定义的路由，默认是关闭状态
> 
> **包括所有网络**
> 
> > 如果开启，所有网络流量都会通过隧道进行路由，但有以下排除项
> > 
> > * **包括本地网络**：如果开启，所有发送到本地网络的流量都将包含在隧道中
> > * **包括APNs**：如果开启，苹果的推送通知服务（APNs）的网络流量将包含在隧道中
> > * **包括蜂窝服务**：如果开启，来自蜂窝服务的互联网可路由网络流量（VoLTE、Wi-Fi通话、IMS、MMS、视觉语音信箱等）将包含在隧道中

### [前置代理](#使用目录)

> 设置 - 代理 - 前置代理
> 
> 「前置代理」表示所有流量先通过 HTTP/SOCKS5 代理转发，再根据配置规则向节点服务器发送请求

### [代理共享](#使用目录)

> 代理共享指的是将你当前配置的代理设置分享给其他设备使用。通过代理共享，你可以把自己配置好的代理服务器（如Shadowsocks、Vmess等）通过局域网或者热点网络的方式让其他设备也能够通过相同的代理设置访问互联网
> 
> **在局域网条件下**
> > * A设备：设置 - 代理 - 代理共享 - 启用共享
> > * B设备：系统设置 - WiFi - WiFi 名称后面 `ⓘ` - HTTP代理 - 手动输入Shadowrocket「代理共享」的IP和端口
> 
> **使用热点条件下**
> > * A设备：开启热点
> > * B设备：连接热点
> > * 然后按照局域网条件下方法进行设置<br>
> >   `此处需要注意下操作顺序，原理是连接设备热点后先形成局域网环境，然后按照局域网条件进行设置`
> >
> **备注**
> > * 如果配置文件开启了 HTTPS 解密，请确保其他设备已安装并信任相同的证书才能正常使用。当其他设备不需要使用解密功能时，可以在“代理共享”页面关闭「HTTPS解密」开关<br>
> > * Telegram 可能不被系统代理接管，可单独在应用内添加 SOCKS5 代理

### [检测代理](#使用目录)

> 如果在使用 Shadowrocket 的时候，遇到某些 APP 提示需关闭代理才能使用，可以在 Shadowrocket - `设置` - `代理类型` - 选择 `None`

### [代理类型](#使用目录)

> Shadowrocket 代理类型：
> 
> * 设置 - 代理 - 代理类型
> 
> * **HTTP**：系统代理模式，对于不支持的程序会交给 tun 接管网络连接
> 
> * **None**：tun模式，全部网络请求都将通过 tun 接口进行处理

### [开启UDP转发](#使用目录)

> * 设置 - UDP - 开启转发- 打开
> 
> * 首页 - 订阅后面 `ⓘ` - UDP转发 - 打开
> 
> * 首页 - 节点后面 `ⓘ` - UDP转发 - 打开

### [隐藏VPN图标](#使用目录)

> 设置 - 排除路由 0.0.0.0/31 - 打开
> 
> 注意：该选项其实是利用系统漏洞实现的，打开开关有一定可能导致网络异常。如遇问题，请关闭此项

### [GEOIP数据库](#使用目录)

> 设置 - GeoLite2 数据库
> 
> 方法一
> * 填写 [MaxMind官网](https://www.maxmind.com) 注册的账户 ID 和密钥，点击下方的`更新`按钮
> 
> 方法二
> * 关注 GitHub 的 IP 数据库项目，复制 mmdb 格式的下载链接，粘贴在国家/ASN 对应的 URL 位置，点击`更新`按钮。当点击`重置`时，可以恢复为系统自带的数据库
> 
>   [Loyalsoldier](https://github.com/Loyalsoldier/geoip) 的 IP 数据库：
>   ```
>   https://raw.githubusercontent.com/Loyalsoldier/geoip/release/Country.mmdb
>   ```
>   [Hackl0us](https://github.com/Hackl0us/GeoIP2-CN) 的 IP 数据库：
>   ```
>   https://github.com/Hackl0us/GeoIP2-CN/raw/release/Country.mmdb
>   ```
>   [Masaiki](https://github.com/Masaiki/GeoIP2-CN) 的 IP 数据库：
>   ```
>   https://github.com/Masaiki/GeoIP2-CN/raw/release/Country.mmdb
>   ```
>   [P3TERX](https://github.com/P3TERX/GeoLite.mmdb) 的 ASN 数据库：
>   ```
>   https://github.com/P3TERX/GeoLite.mmdb/raw/download/GeoLite2-ASN.mmdb
>   ```

### [自动更新](#使用目录)

> 现阶段软件的自动更新包含配置文件自动更新、服务器订阅自动更新以及 `GeoLite2 数据库` 自动更新。需要在 `系统设置 - 通用 - 后台App刷新` 中为 Shadowrocket 启用后台刷新
> 
> * **配置**：自动 [更新配置](#更新配置) 功能。该功能可根据设置自动更新当前配置文件以及当前所用的规则集、脚本等远程资源。若当前配置文件使用的是从远程链接加载的，更新配置文件会使用原远程链接拉取全新配置替换当前配置，该操作会覆盖对该配置文件做过的所有自定义设置；若当前配置文件是默认配置或不含更新地址的配置文件，则自动更新功能仅会更新当前所用的规则集、脚本等远程资源
> 
>     * 自动后台更新：开启后可根据设置自动更新配置文件
>     * 更新提醒：开启后，更新时会弹出相应提醒。需要开启设备推送通知
>     * 更新间隔：单位为  `天`，可选 1-7 天
>     * 规则集/脚本资源手动更新方法：点击配置文件 - 使用配置
>     * 小技巧：若当前配置是远程配置，希望自动更新规则集等远程资源且不希望自定义设置被覆盖，可进入 [纯文本编辑](#编辑纯文本) 删除或注释掉 `update-url = *` 行
>   
> * **订阅**：[参见此处](#更新订阅节点)
> * **GeoLite2 数据库**：包含自动后台更新选项、更新提醒选项、更新间隔选项，其中更新间隔单位为 `天` 。其他设置 [参见此处](#GEOIP数据库)

------

## [其他问题](#其他问题)

### [自动切换节点](#使用目录)

> 自动切换延迟低的节点：
> 
> **方法一**
> > * 首页 - 全局路由 - 分组 - 简单模式 - 打开
> 
> **方法二**
> > * 点击配置文件 `ⓘ` - 代理分组 - 右上角 `➕` - 类型`url-test`
> 
> **备注**
> > * 如果节点不稳定，可同时 [开启回退](#启用回退)

### [SSL错误](#使用目录)

> 添加/更新订阅链接时，如果提示 `发生了 SSL 错误，无法建立与该服务器的安全连接`，可以尝试的解决方法：
> 
> * 全局路由选代理，使用另外一个节点来添加/更新订阅链接
> 
> * 切换网络后再添加/更新订阅链接
> 
> * 检查订阅链接是否错误或失效

### [节点旗帜](#使用目录)

> 节点优先根据备注名称匹配旗帜，如果匹配不成功，由节点地址解析出 IP，通过数据库判断该IP的国家或地区，然后显示对应的旗帜
> 
> * 节点后面 `ⓘ` - 地址栏的图标，可以手动修改旗帜
> * 订阅后面 `ⓘ` - 订阅链接后面 `ⓘ`，利用脚本也能批量修改旗帜
> 
> 如果把旗帜的 Emoji 放在节点备注开头，保存时会自动显示对应的旗帜

### [节点感叹号](#使用目录)

> 节点显示感叹号原因：
> 
> * 您的节点使用了 TLS，地址是 IP，却没有设 SNI
> 
> 这不是正确的服务器设置，但为了可以正常连接，Shadowrocket 会主动开启 `允许不安全`。`允许不安全` 将跳过TLS证书验证，这将导致一些安全问题。如果您使用自签名证书，请将证书导入系统并信任它，否则请及时续订服务器端证书，以防止证书过期。在 `2.2.23` 等特定版本中，该选项可能默认为关闭状态

### [微信转圈](#使用目录)

> 如果使用 Shadowrocket 时微信一直显示 `连接中/收取中`，可以尝试的解决方法：
> 
> * 微信分流走直连
> 
> * 点击配置文件 `ⓘ` - 通用 - 启用IPv6 - 关闭
>   
> 本质上该问题是由于使用的分流对 IPv6 分流不恰当，可能造成国内的部分 IPv6 地址被错误地分流至代理隧道造成的

### [模块消失](#使用目录)

> 模块页面已经开启 `保存到iCloud`，如果出现模块消失的问题，请检查：
> 
> * 系统设置 - Apple ID - iCloud - 使用iCloud的APP中，确保Shadowrocket/iCloud云盘已经打开同步
> 
> * 文件app - iCloud云盘 - Shadowrocket，确定其中包含 `Modules` 和 `Script` 两个子文件夹
> 
> * 文件app - iCloud云盘 - Shadowrocket - Modules，如果iCloud的本地缓存被清理，此时模块文件是未下载状态，请等待自动下载或手动下载

### [VPN自动断开](#使用目录)

> 系统版本低于 `iOS 15` 处理复杂请求、加解密数据、运行脚本等因素相互作用之下可能导致 NE 内存占用过高，从而造成 VPN 自动断开，解决方法：
> 
> `设置` - `按需求连接` - 打开 `始终开启`

### [定位权限](#使用目录)

> * iOS 系统的要求，开启定位权限才能获取 Wi-Fi 名称
> 
> * 如果不需要在 Shadowrocket 里看到 Wi-Fi 信息，那么就可以不用开启

### [编译原因](#使用目录)

> Shadowrocket 2.2.29 之前的版本是使用 Xcode 13.2.1 编译的
> 
> 2023年4月份以后，苹果官方要求开发者在提交应用到 App Store 时必须至少使用 Xcode 14 编译，所以 iOS12 以下系统无法使用
> 
> Shadowrocket 在版本 `2.2.30` 之后设置最低安装要求 iOS12，然后停止 `2.2.29` 版本，iOS 低版本用户可以安装 `2.2.28` 版本

### [下载Shadowrocket](#使用目录)

> Shadowrocket 只有 `iOS/iPadOS/tvOS` 版本和 M 系列芯片的 Mac 才能下载，开发者是 `Shadow Launch Technology Limited`。**Shadowrocket没有 安卓/Windows 版本！**
> 
> 下载方法：
> * 非国区 ID 登陆 App Store，搜索 Shadowrocket，购买后下载<br>
> * Shadowrocket 是买断制的付费软件<br>
> * 美区价格：2.99 美元<br>
> * 使用美区 ID 时，地址建议填免税州
>   ```
>   五个免税州：
>   俄勒冈州（Oregon）
>   蒙大拿州（Montana）
>   特拉华州（Delaware）
>   新罕布什尔州（New Hampshire）
>   阿拉斯加州（Alaska）部分区域
>   ```
> 
> [美国地址生成器](https://www.meiguodizhi.com)<br>
> [美区 Apple ID 注册方法](https://blog.skylershu.com/post/apple-id-us-2022)<br>
> [Apple 官网购买礼品卡方法](https://blog.skylershu.com/post/apple-gift-card)<br>
> [Shadowrocket 下载链接](https://apps.apple.com/app/shadowrocket/id932747118)

### [URL-Schemes](#使用目录)

请使用相应内容直接替换代码中的大括号及其内容

> `启动 VPN 隧道` 
> ```ruby
> shadowrocket://connect
> ```
> ```ruby
> shadowrocket://open
> ```
>  `停止 VPN 隧道` 
> ```ruby
> shadowrocket://disconnect
> ```
> ```ruby
> shadowrocket://close
> ```
>  `切换 VPN 开关状态` 
> ```ruby
> shadowrocket://toggle
> ```
>  `使用特定节点` 
> ```ruby
> shadowrocket://select?s={节点名称}
> ```
>  `添加 订阅/节点` 
> ```ruby
> shadowrocket://add/{url}
> ```
>  `安装/使用 配置` 
> ```ruby
> shadowrocket://config/add/{url}
> ```
>  `安装/使用 模块` 
> ```ruby
> shadowrocket://install?module={url}
> ```
>  `切换全局路由（代理/配置/直连/场景）` 
> ```ruby
> shadowrocket://route/proxy
> ```
> ```ruby
> shadowrocket://route/config
> ```
> ```ruby
> shadowrocket://route/direct
> ```
> ```ruby
> shadowrocket://route/scene
> ```
> `安装/使用 配色` 
> ```ruby
> shadowrocket://color?{配色设置}
> ```

------
