# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build & Run

```bash
mkdir -p build && cd build
cmake ..
make
```

Produces two C++ executables: `match_system/match_system` (port 9090) and `database/database` (port 7070).

Dependencies: Apache Thrift C++ library, pkg-config, pthreads. Python client also needs `thrift` pip package.

Start services in order (separate terminals):
1. `./database/database` — persistence server (TSimpleServer on port 7070)
2. `./match_system/match_system` — match server (TThreadedServer on port 9090)
3. `cd game/src && python3 client.py` — game client (reads stdin)

Client stdin format: `add <user_id> <user_name> <score>` / `remove <user_id> <user_name> <score>`

## Architecture

This is a Thrift RPC game matchmaking system with three components:

```
[client.py] —add/remove RPC→ [match_system] —save_data RPC→ [database] → result.txt
```

**Thrift IDL** (`thrift/`): `match.thrift` defines `User` + `Match` service (add/remove). `save.thrift` defines `Save` service (save_data). Generated code is checked into each component's source tree.

**match_system** (`match_system/src/match_system.cpp`): Multi-threaded C++ match server. Core classes in the single source file:
- `Pool` — maintains `users[]` (active), `users_wt[]` (all), `wait_cnt` per player. `match()` runs every ~1s, incrementing wait counters each round. Matching threshold = `wait_cnt * 50` score points — players waiting longer get matched more aggressively.
- `Task` / `MessageQueue` — producer-consumer pattern. RPC handler threads push add/remove tasks; a single background `consume_task()` thread pops and applies them.
- `MatchHandler` / `MatchCloneFactory` — Thrift `TThreadedServer` machinery (thread-per-connection factory).
- `Pool::save_result()` calls the `Save` Thrift client on `localhost:7070`.

**database** (`database/src/database.cpp`): Simple persistence server. `SaveHandler::save_data()` appends match results to `result.txt`. Uses `TSimpleServer`.

**game client** (`game/src/client.py`): Python script reading stdin, calling `add_user()`/`remove_user()` on the match server via Thrift.

All server ports, addresses, and save credentials are hardcoded in the source — there are no config files.

---

# CLAUDE.md（中文版）

本文件为 Claude Code (claude.ai/code) 在此仓库中工作时提供指引。

## 构建与运行

```bash
mkdir -p build && cd build
cmake ..
make
```

生成两个 C++ 可执行文件：`match_system/match_system`（端口 9090）和 `database/database`（端口 7070）。

依赖：Apache Thrift C++ 库、pkg-config、pthreads。Python 客户端还需要 `thrift` pip 包。

按顺序启动服务（分别在独立终端中）：
1. `./database/database` — 持久化服务器（TSimpleServer，端口 7070）
2. `./match_system/match_system` — 匹配服务器（TThreadedServer，端口 9090）
3. `cd game/src && python3 client.py` — 游戏客户端（从标准输入读取）

客户端输入格式：`add <用户ID> <用户名> <分数>` / `remove <用户ID> <用户名> <分数>`

## 架构

这是一个基于 Thrift RPC 的游戏玩家匹配系统，包含三个组件：

```
[client.py] —add/remove RPC→ [match_system] —save_data RPC→ [database] → result.txt
```

**Thrift IDL**（`thrift/` 目录）：`match.thrift` 定义了 `User` 结构体和 `Match` 服务（add/remove 接口）。`save.thrift` 定义了 `Save` 服务（save_data 接口）。生成的代码已直接提交到各组件的源码目录中。

**match_system**（`match_system/src/match_system.cpp`）：多线程 C++ 匹配服务器。所有核心类集中在单个源文件中：
- `Pool` — 维护 `users[]`（活跃玩家）、`users_wt[]`（全部玩家）、每个玩家的 `wait_cnt`。`match()` 约每 1 秒执行一次，每轮递增等待计数器。匹配阈值 = `wait_cnt * 50` 分差 — 等待时间越长的玩家，匹配范围越宽松。
- `Task` / `MessageQueue` — 生产者-消费者模式。RPC 处理线程将 add/remove 任务推入队列；单个后台 `consume_task()` 线程取出任务并执行匹配。
- `MatchHandler` / `MatchCloneFactory` — Thrift `TThreadedServer` 机制（每连接一线程的工厂）。
- `Pool::save_result()` 调用 `Save` Thrift 客户端连接 `localhost:7070`。

**database**（`database/src/database.cpp`）：简单的持久化服务器。`SaveHandler::save_data()` 将匹配结果追加写入 `result.txt`。使用 `TSimpleServer`。

**game client**（`game/src/client.py`）：Python 脚本，从标准输入读取命令，通过 Thrift 调用匹配服务器的 `add_user()`/`remove_user()`。

所有服务器端口、地址和保存凭据均硬编码在源码中 — 没有配置文件。
