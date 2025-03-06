[![Shadowrocket](https://socialify.git.ci/LOWERTOP/Shadowrocket/image?custom_description=User%20Manual&description=1&font=Rokkitt&forks=1&logo=https%3A%2F%2Fraw.githubusercontent.com%2FLOWERTOP%2FShadowrocket-First%2Frefs%2Fheads%2Fmain%2Fimg%2FShadowrocket.png&name=1&pattern=Plus&stargazers=1&theme=Light)](https://github.com/LOWERTOP/Shadowrocket "Repository URL")

[![README in Chinese](https://img.shields.io/static/v1?label=&message=README%20in%20Chinese&color=blue&logo=googletranslate&logoColor=white&labelColor=blue&messageColor=white)](https://lowertop.github.io/Shadowrocket "Chinese")

> [!NOTE]
> 
> The original repository for the "Lazy Config" series and keyword lists has been deactivated. This repository will maintain its final version and possible subsequent updates, with plans to gradually refine the original keyword lists into a comprehensive manual. The [Original branch](https://github.com/LOWERTOP/Shadowrocket/tree/Original) contains legacy files. The [Johnshall's Repository](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever) will continue updates based on this repository. For other needs, refer to the **[Theme & Config Repository](https://github.com/LOWERTOP/Shadowrocket-First)** <br>
> We sincerely thank the original authors and all contributors to related projects!

------

# [Shadowrocket User Manual](https://lowertop.github.io/Shadowrocket/ "Release Page")

> [!NOTE]
> 
> **[Shadowrocket](https://apps.apple.com/us/app/shadowrocket/id932747118)** is a network proxy tool developed by **[Shadow Launch Technology Limited](https://shadowlaunch.com/)** for iOS devices, also supporting Apple TV and Mac (M-series chips Only). It offers flexible configuration options to forward device traffic through proxy servers, helping users bypass network restrictions, access blocked content, enhance privacy, 和 meet diverse needs.

> [!TIP]
> 
> **Quick Start**
> 
> > * Home > Add Node
> > * Settings > Latency Test Method > **`CONNECT`**
> > * Home > Connectivity Test, then select an available node.
> 
> On first launch, you will be prompted to **`Install VPN Profile`**. Click **`Allow`** to proceed.

## [Table of Contents](#table-of-contents)
> [!TIP]
> * Click **section titles** to jump to content.
> * Click **blue titles** in content to return to the table of contents.

> * [主页](#home)
>     * [Add Node](#add-node)
>     * [Add WireGuard Node](#add-wireguard-node)
>     * [Update Subscription Nodes](#update-subscription-nodes)
>     * [Node Sorting](#node-sorting)
>     * [Node Sharing & Management](#node-sharing--management)
>     * [Subscription Node Filtering](#subscription-node-filtering)
>     * [Proxy Chain](#proxy-chain)
>     * [Global Routing Modes](#global-routing-modes)
>     * [Connectivity Test](#connectivity-test)
>     * [Modify Test Address](#modify-test-address)
>     * [Scenarios](#scenarios)
>     * [Simple Mode](#simple-mode)
>     * [Enable Fallback](#enable-fallback)
> * [Configurations](#configurations)
>     * [Configuration Files](#configuration-files)
>     * [Apply Configuration](#apply-configuration)
>     * [Edit Configuration](#edit-configuration)
>     * [Edit Plain Text](#edit-plain-text)
>     * [Preview Configuration](#preview-configuration)
>     * [Update Configuration](#update-configuration)
>     * [Rename](#rename)
>     * [Export Configuration](#export-configuration)
>     * [Extended Configuration](#extended-configuration)
>     * [General Parameters](#general-parameters)💡
>     * [Add Rules](#add-rules)
>     * [Rule Priority](#rule-priority)
>     * [Rule Types](#rule-types)
>     * [Rule Policies](#rule-policies)
>     * [App-Based Routing](#app-based-routing)
>     * [Update Rule Sets](#update-rule-sets)
>     * [Preview Rule Sets](#preview-rule-sets)
>     * [Modify DNS](#modify-dns)
>     * [DNS-over-PROXY](#dns-over-proxy)
>     * [no-resolve Function](#no-resolve-function)
>     * [Proxy Groups/Policy Groups](#proxy-groups-policy-groups)
>     * [Proxy Group Types](#proxy-group-types)
>     * [Script URLs](#script-urls)
>     * [Rule Set URLs](#rule-set-urls)
>     * [Copy Configuration](#copy-configuration)
>     * [Hosts](#hosts)
>     * [URL Rewrite](#url-rewrite)
>     * [HTTPS Decryption](#https-decryption)
>     * [Load Balancing](#load-balancing)
>     * [Modules](#modules)
>     * [Certificate Module](#certificate-module)
>     * [Identity Certificate Password](#identity-certificate-password)
> * [Data](#data)
>     * [Proxy Logs](#proxy-logs)
>     * [DNS Logs](#dns-logs)
>     * [iCloud Auto-Sync](#icloud-auto-sync)
>     * [Node Data Management](#node-data-management)
>     * [Traffic Statistics](#traffic-statistics)
> * [Settings](#settings)
>     * [Latency Test Method](#latency-test-method)
>     * [Widgets](#widgets)
>     * [On-Demand Connection](#on-demand-connection)
>     * [Tunnels](#tunnels)
>     * [Upstream Proxy](#upstream-proxy)
>     * [Proxy Sharing](#proxy-sharing)
>     * [Proxy Detection](#proxy-detection)
>     * [Proxy Type](#proxy-type)
>     * [Enable UDP Forwarding](#enable-udp-forwarding)
>     * [Hide VPN Icon](#hide-vpn-icon)
>     * [GEOIP Database](#geoip-database)
>     * [Auto-Update](#auto-update)
>     * [Graceful Policy Mechanism](#graceful-policy-mechanism)
> * [Miscellaneous](#miscellaneous)
>     * [Auto-Switch Nodes](#auto-switch-nodes)
>     * [SSL Errors](#ssl-errors)
>     * [Node Flags](#node-flags)
>     * [Node Exclamation Mark](#node-exclamation-mark)
>     * [WeChat Loading Issues](#wechat-loading-issues)
>     * [Missing Modules](#missing-modules)
>     * [Module Failure](#module-failure)
>     * [VPN Auto-Disconnect](#vpn-auto-disconnect)
>     * [Location Permissions](#location-permissions)
>     * [Compilation Notes](#compilation-notes)
>     * [Download Shadowrocket](#download-shadowrocket)
>     * [URL-Schemes](#url-schemes)

------

## [Home](#home)

### [Add Node](#table-of-contents)

> * Home > Top-left > Scan QR Code
>   
> * Copy node links (e.g., `trojan://*`, `vmess://*`, `vless://*`). Shadowrocket will auto-import when opened.
>   
>   `Requires clipboard access permission`
> 
> * Home > Top-right `➕` > Type `Subscribe` > Enter subscription URL > Save
> 
>   `Add "#1", "#2", "#3" to the subscription URL to add duplicates`
> 
> * Home > Top-right `➕`, select protocol type, fill in node details, and save.
> 
>   **Supported protocols**: `Shadowsocks, ShadowsocksR, Subscribe, Vmess, VLESS, Relay, Socks5, Socks5 Over TLS, HTTP, HTTPS, HTTP2, Trojan, Hysteria, Hysteria2, TUIC, Juicity, WireGuard, Snell v2, Brook, Lua`

### [Add WireGuard Node](#table-of-contents)

> * Home > Top-right `➕` > Type `WireGuard`, fill in config details.
> 
> * Copy WireGuard config in the following format. Shadowrocket will auto-detect and prompt for import:
>   
>   ```ruby
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
>   If not auto-detected, check if `Allow Clipboard Detection` is enabled in settings, or manually paste via the `Paste` button below the connectivity test.

### [Update Subscription Nodes](#table-of-contents)

> * Swipe left on subscription > Update
> 
> * Tap the refresh button 🔄 on Home
> 
> * Settings > Subscriptions > Update on Launch (reopen app to auto-update)
> 
> * Settings > Subscriptions > Auto-Background Update (enable in system `Settings > General > Background App Refresh`, cycle: 1-24 hours)
> 
> * Use Shadowrocket's Shortcuts for automated updates
> 
> * Long-press app icon > Update Subscriptions
>   
> 
> **Common errors**:
> * **Forbidden**: Subscription reset or token error
> * **Not Found**: Incorrect path
> * **Service Unavailable**: Domain blocked or incorrect

### [Node Sorting](#table-of-contents)

> Settings > Subscriptions > Sort by `Ping`

### [Node Sharing & Management](#table-of-contents)

> **Sharing Nodes**
> 
> > * Long-press node > Copy to share via link
> > 
> > * Swipe left on node > QR Code. Other devices can scan to add (use `Share` button to send QR)
> > 
> >   `QR standards vary. Some Vmess nodes may lose info when scanned by other tools. Verify configs if issues occur`
> > 
> > * Tap node's `ⓘ` > Scroll to bottom for sharing options
> > 
> > * Tap `•••` > Select nodes > Copy to share multiple
> 
> **Node Management**
> 
> > * **Reorder**: Tap `•••` > Drag `≡` icon
> > 
> > * **Categorize**: Use `Collapse` to group local nodes
> > 
> > * **Delete**: Tap `•••` > Delete All/Timeout Nodes
> > 
> > * **Swipe Actions**: Swipe right on node to `Test` or `Copy`

### [Subscription Node Filtering](#table-of-contents)

> **Filtering**
> 
> > Home > Tap `ⓘ` on subscription > Filter
> > 
> > `Use regex without "/"`
> > 
> > * Include nodes with keywords A and B:
> >   ```ruby
> >   /(?=.*(A))^(?=.*(B))^.*$/
> >   ```
> > * Include A or B:
> >   ```ruby
> >   A|B
> >   ```
> > * Exclude A or B:
> >   ```ruby
> >   /^((?!(A|B)).)*$/
> >   ```
> > * Include A but exclude B:
> >   ```ruby
> >   /(?=.*(A))^((?!(B)).)*$/
> >   ```
> 
> **Batch Scripts**
> 
> > * Replace keyword a with b:
> >   ```ruby
> >   $server.title=$server.title.replace(/a/g,'b')
> >   ```
> > * Add prefix:
> >   ```ruby
> >   $server.title='abc'+$server.title
> >   ```
> > * Enable reserved ports:
> >   ```ruby
> >   $server.reserved="1,40-60,30-50"
> >   ```
> > * Enable multiplexing:
> >   ```ruby
> >   $server.mux=1
> >   ```
> > * Set proxy chain:
> >   ```ruby
> >   $server.chain="Subscription/Node"
> >   ```
> 
> **Advanced Scripts**: Refer to [examples](https://github.com/LOWERTOP/Shadowrocket-First#filter-scripts)

### [Proxy Chain](#table-of-contents)

> Route traffic through another proxy (supports multi-level chains):
> 
> * Node A > `ⓘ` > Proxy Via > Node B. Path: `Client > B > A > Web`
> * Use entire subscription as chain (random node selected). Check logs for `backend chain`
> * Cancel chain: `ⓘ` > Proxy Via > Cancel

### [Global Routing Modes](#table-of-contents)

> * **Config**: Traffic routed per rules
> * **Proxy**: All traffic via one node
> * **Direct**: No proxy
> * **Scenario**: Auto-switch mode based on network type (Wi-Fi/Cellular)

### [Connectivity Test](#table-of-contents)

> Home > `Connectivity Test` shows latency in ms. Test methods:
> 
> Settings > Latency Test Method:
> 
> * **TCP**: TCP handshake time
> * **ICMP**: ICMP echo round-trip
> * **CONNECT**: HTTP HEAD request (recommended)
> 
> Use <https://www.speedtest.net> for speed tests.

### [Modify Test Address](#table-of-contents)

> **For Home/Group Tests**:
> 
> > * Settings > Latency Test Method > URL Settings
> > * Home > Tap circular icon next to test > URL Settings
> 
> **For Proxy Groups**:
> 
> > * Configuration > Proxy Group > Edit > URL field

### [Scenarios](#table-of-contents)

> Auto-switch routing based on network type:
> > * Home > Global Routing > Scenarios > Add
> > * Set mode (Config/Direct/Proxy) per network (Wi-Fi/Cellular)
> > * For multiple cellular interfaces, check `Settings > Diagnostics > Network`
> 
> Location permission may be required. Scenarios work without permission but won’t auto-switch indicators.

### [Simple Mode](#table-of-contents)

> Auto-test and switch to low-latency nodes:
> 
> * Home > Global Routing > Group > Simple Mode
> 
> **Node Range**: All nodes or selected group
> 
> **Test Interval**: Default 600s (10 mins)
> 
> **Tolerance**: Lower tolerance triggers more frequent switches
> 
> **Proxy Policy**: Routes all `proxy`-tagged rules

### [Enable Fallback](#table-of-contents)

> Home > Global Routing > Enable Fallback
> 
> * Switches nodes after 3 failures
> * Random selection within `proxy` or group nodes
> * Check [Proxy Logs](#proxy-logs) for details

------

## [Configurations](#configurations)

### [Configuration Files](#table-of-contents)

> Config files (`.conf`) simplify setup and sync across devices. The default `default.conf` is updated with app releases. Restore via `Config > Restore Default`.
> 
> **Add Config**:
> > * From URL: `Config > ➕ > Paste URL > Download`
> > * From local/cloud: `Config > Import from Cloud`
> 
> **Actions**:
> > * [Apply Configuration](#apply-configuration)
> > * [Edit Configuration](#edit-configuration)
> > * [Edit Plain Text](#edit-plain-text)
> > * [Preview Configuration](#preview-configuration)
> > * [Update Configuration](#update-configuration)
> > * [Extended Configuration](#extended-configuration)
> > * [Rename](#rename)
> > * [Export Configuration](#export-configuration)

### [Apply Configuration](#table-of-contents)

> Tap `Apply` to enable and update remote resources (rule sets, scripts).

### [Edit Configuration](#table-of-contents)

> Modify settings via UI. Advanced options require [plain text editing](#edit-plain-text).

### [Edit Plain Text](#table-of-contents)

> Directly edit config text. Reference:
> > * [Lazy Config](https://raw.githubusercontent.com/LOWERTOP/Shadowrocket/main/lazy.conf)
> > * [Lazy Config (with Groups)](https://raw.githubusercontent.com/LOWERTOP/Shadowrocket/main/lazy_group.conf)

### [Preview Configuration](#table-of-contents)

> View raw text of remote configs (available only for remote configs).

### [Update Configuration](#table-of-contents)

> Update remote config and resources (for remote configs). See [Auto-Update](#auto-update).

### [Rename](#table-of-contents)

> Rename the config file.

### [Export Configuration](#table-of-contents)

> Export config as a file.

### [Extended Configuration](#table-of-contents)

> Config B inherits from Config A. Modify via `Config > ⓘ > General > Include Config`.

### [General Parameters](#table-of-contents)

> **Bypass System**: Disabling may cause system issues (e.g., delayed notifications)
> 
> **Skip Proxy**: Force traffic through TUN instead of proxy (fixes app compatibility)
> 
> **TUN Bypass Routes**: Bypass non-TCP protocols
> 
> **DNS Override**: Use custom DNS (e.g., DoH, DoT)
> 
> **Fallback DNS**: Used if override fails (default: system DNS)
> 
> **IPv6 Support**: `false` to disable. Node domains with IPv6 will still use IPv6 unless blocked via `[Host]`.
> 
> **Prefer IPv6**: `false` by default
> 
> **Private IP Answer**: Block domains resolving to private IPs
> 
> **TUN Included Routes**: Add smaller routes for TUN handling
> 
> **Always Real IP**: Return real IPs in DNS queries
> 
> **DNS Hijacking**: Redirect hardcoded DNS
