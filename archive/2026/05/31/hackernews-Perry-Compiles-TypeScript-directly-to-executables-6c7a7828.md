---
title: "Perry Compiles TypeScript directly to executables using SWC and LLVM"
source: Hacker News
url: https://www.perryts.com/
date: 2026-05-31
published_at: 2026-05-30T03:14:25+00:00
tag: 工具开源
item_id: 6c7a7828dd272d9c
---
# One Codebase. Every Platform.

Native Performance.

Perry compiles TypeScript to native GUI and CLI apps on macOS, iPadOS, iOS, Android, Linux, Windows, watchOS, tvOS, WebAssembly, and the Web. No runtime. No Electron. Just native binaries.

$ perry compile main.ts

Compiling main.ts...

✓ Compiled executable: main (2.3 MB)

$ ./main

Hello, World!

Real apps, compiled from TypeScript with Perry.

[View all showcase projects](https://www.perryts.com/en/showcase/)

## Why Perry?

Everything you need to compile TypeScript to native applications

### No Runtime Required

Produces standalone native executables. No Node.js, no V8, no runtime dependencies. Just a single binary that runs anywhere.

### Fast Compilation

Direct TypeScript to native code compilation using SWC for parsing and LLVM for optimized code generation. No intermediate JavaScript.

### Small Binaries

Output binaries are typically 2-5MB. With optional V8 runtime for JS npm packages, 15-20MB. Ship less, deploy faster.

### Deterministic Builds

Same input, same binary. Reproducible across machines, across CI runs, across teams. No mystery rebuilds.

### Comprehensive Standard Library

Built-in native implementations of fs, path, crypto, os, Buffer, child_process, and more. Use familiar Node.js APIs.

### Optional V8 Runtime

Need to use a pure JavaScript npm package? Enable the V8 runtime flag for full npm ecosystem compatibility.

### 25+ Native UI Widgets

Buttons, text fields, text areas, tables, canvas, scroll views, QR codes, secure fields, splash screens, and more — all compiling to real platform widgets via AppKit, GTK4, Win32, UIKit, and JNI.

### Compile-Time Plugin System

Modules compose at build time — no runtime plugin overhead, no IPC boundaries. Your dependencies become direct native function calls in the final binary.

### True Multi-Threading

Real OS threads with parallelMap, parallelFilter, and spawn. Compile-time safety rejects mutable captures — no SharedArrayBuffer, no workers, just threads.

### Compile-Time i18n

Automatic string extraction, CLDR plural rules for 30+ locales, compile-time validation. Translations baked into the binary with near-zero runtime lookup.

## Native on Every Platform

Perry compiles your TypeScript to native UI frameworks, WebAssembly, and JavaScript — not web views, not Electron. Real native widgets on every platform, plus the web.

### macOS

AppKit

### iOS

UIKit

### iPadOS

UIKit

### Android

Views

### Linux

GTK4

### Windows

Win32

### watchOS

SwiftUI

### tvOS

SwiftUI

### WASM

WebAssembly

### Web

JavaScript

## From Code to App Store

Perry doesn't just compile your app — it gets it into your users' hands.

### Build & Sign

Cross-platform builds from one command. Code signing for macOS, iOS, Android, and Windows handled for you. No wrestling with Xcode provisioning profiles or Android keystores.

### Distribute

Push to the App Store, Play Store, or ship direct downloads. Perry Publish handles packaging, notarization, and submission.

### Verify

Powered by Geisterhand. Automated UI testing across all 6 platforms. Know your app works everywhere before your users tell you it doesn't.

Free for open-source projects. [Plans for teams](https://www.perryts.com/en/publish/) → /publish

## The only framework that checks every box

TypeScript compiled to native code. Real platform widgets. No runtime overhead.

| Framework | Language | Native Code | Native Widgets | Runtime Overhead |
|---|---|---|---|---|
Perry★AOT compiled to native binary | TypeScript | None | ||
React NativeJIT / interpreted at runtime | JS / TypeScript | Hermes / V8 + Bridge | ||
FlutterAOT compiled, custom renderer | Dart | Dart VM + Skia engine | ||
KMP + ComposeJVM on Android, native on iOS | Kotlin | Partial | Kotlin runtime + Skia | |
Swift for AndroidNative binary, no shared UI | Swift | No shared UI | Swift runtime on Android | |
.NET MAUIPartial AOT via Mono | C# | Partial | .NET / Mono runtime | |
NativeScriptJS runtime, native widget access | JS / TypeScript | V8 / JavaScriptCore | ||
IonicWeb app in native wrapper | JS / TypeScript | WebView + Capacitor |

## Write TypeScript, Ship Native

Use familiar TypeScript syntax and APIs. Perry handles the rest.

`// hello.tsconst greeting = "Hello, World!";console.log(greeting); // Compiles to ~2MB native executable// No runtime needed!`


## Performance Comparison

Native compilation delivers unmatched efficiency

| Metric | Perry | Node.js | Bun |
|---|---|---|---|
| Binary Size | 2-5 MB | ~80 MB | ~90 MB |
| Startup Time | ~1 ms | ~30 ms | ~10 ms |
| Runtime Dependencies | None | Node.js | Bun |
| Memory Overhead | Minimal | V8 + GC | JSC + GC |

### Benchmark Results: Up to 18x Faster

Perry v0.5.279 vs Node.js v25 — RUNS=11 median, Apple M1 Max (lower is better)

## Get Started

Install Perry and start compiling TypeScript to native executables

### 1Installation

`$ brew tap PerryTS/perry`

`$ brew install perry`

Requires Homebrew. Supports macOS arm64 and x86_64.

### 2Usage

`perry compile main.ts`

Compiles main.ts to a native executable

`perry compile main.ts -o myapp`

Specify the output executable name

`perry compile main.ts --enable-js-runtime`

Enable V8 for JavaScript npm package compatibility

`perry check ./src`

Validate TypeScript code for native compilation

## Feature Support

Comprehensive TypeScript and Node.js API coverage

### Core Language

- Numbers64-bit floating point (f64)
- StringsUTF-8, all common methods
- Booleanstrue/false, logical operators
- ArraysTyped and mixed-type arrays
- ObjectsObject literals and field access
- BigInt256-bit integer support
- EnumsNumeric and string enums

### Functions

- Function DeclarationNamed functions
- Arrow Functions() => {} syntax
- Default ParametersParameters with defaults
- Rest Parameters...args syntax
- ClosuresIncluding mutable captures
- Higher-Order FunctionsFunctions as arguments/returns
- Async/AwaitAsync function support

### Classes

- Class DeclarationBasic class syntax
- ConstructorsWith parameters
- Private Fields (#)ES2022 #privateField syntax
- Static Methods/FieldsClass-level members
- Getters/Settersget/set accessors
- Inheritanceextends keyword
- Super Callssuper() constructor calls

### Type System

- Type AnnotationsExplicit type declarations
- Type InferenceAutomatic type detection
- GenericsMonomorphization (like Rust)
- InterfacesInterface declarations
- Union Typesstring | number support
- Type Guardstypeof operator
- Type Aliasestype X = ... declarations

### Standard Library

- fsreadFileSync, writeFileSync, existsSync, etc.
- pathjoin, dirname, basename, extname, resolve
- cryptorandomBytes, randomUUID, sha256, md5
- osplatform, arch, hostname, memory info
- Bufferfrom, alloc, toString, slice, copy
- child_processexecSync, spawnSync
- JSON/Math/DateFull implementations

## 30+ Native npm Packages

Popular npm packages reimplemented in native Rust. No npm install, no node_modules, just fast native code.

### Database

### Security

### HTTP

### Data Processing

### Date & Time

### Utilities

## How It Works

From TypeScript source to native executable in seconds

Want to know how the compiler works under the hood? [Compiler internals](https://www.perryts.com/en/internals/)
