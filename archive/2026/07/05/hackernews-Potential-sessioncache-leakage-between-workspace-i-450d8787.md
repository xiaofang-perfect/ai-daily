---
title: "Potential session/cache leakage between workspace instances or consumer accounts"
source: Hacker News
url: https://github.com/anthropics/claude-code/issues/74066
date: 2026-07-05
published_at: 2026-07-04T14:03:40+00:00
tag: 行业动态
item_id: 450d878726a4ba28
---
**Bug Description**

Apparent session leakage, despite authenticated to Enterprise ZDR workspace. Agent suddenly started asking me what kind of bricks I wanted for my Minecraft temple and confidently asserted in its recap that it's building a Minecraft temple. I thought cache was isolated to workspace? Maybe one of my colleagues is building a minecraft temple. That's one way to spend your token allowance, I suppose. Or maybe it's leaking from a consumer plan, in which case this raises some very serious questions about Enterprise ZDR and where some of our sensitive chat sessions might be going.

**Environment Info**

- Platform: darwin
- Terminal: Apple_Terminal
- Version: 2.1.199
- Feedback ID: f336f5d2-3992-4a04-9e1f-ec30f006f75e

**Errors**

![Image](https://private-user-images.githubusercontent.com/149510075/617046476-4e1cb6a2-a3c0-4b44-bd29-d42288e85e75.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODMyMzE2ODQsIm5iZiI6MTc4MzIzMTM4NCwicGF0aCI6Ii8xNDk1MTAwNzUvNjE3MDQ2NDc2LTRlMWNiNmEyLWEzYzAtNGI0NC1iZDI5LWQ0MjI4OGU4NWU3NS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNzA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDcwNVQwNjAzMDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03MmY2YjkwNThhNDM5NGVjZTdmN2FlOGFlZTJlZTFhOGRkOTA5Zjg3MzY3MGRmOTlmYzcyY2RiYTMyNDllMDAzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.ynPIag3qnV3sL34WjZZvu_aONQX5e6KMSUQ5lO5Bk7c)

Maybe relevant: I'm doing something kind of weird. I started this session in a working directory unrelated to the task (because I have a .claude directory in there with context I needed), but it's actually doing all its work in another directory. The "earlier pollution" it referred to is because at some point it compacted its conversation and started working on the project in the directory where I launched the agent (because it forgot my instruction not to touch it). That was less surprising and obviously caused by my own setup. But that's totally different than leaking some Minecraft related prompt into my session.

Bug DescriptionApparent session leakage, despite authenticated to Enterprise ZDR workspace. Agent suddenly started asking me what kind of bricks I wanted for my Minecraft temple and confidently asserted in its recap that it's building a Minecraft temple. I thought cache was isolated to workspace? Maybe one of my colleagues is building a minecraft temple. That's one way to spend your token allowance, I suppose. Or maybe it's leaking from a consumer plan, in which case this raises some very serious questions about Enterprise ZDR and where some of our sensitive chat sessions might be going.

Environment InfoErrorsMaybe relevant: I'm doing something kind of weird. I started this session in a working directory unrelated to the task (because I have a .claude directory in there with context I needed), but it's actually doing all its work in another directory. The "earlier pollution" it referred to is because at some point it compacted its conversation and started working on the project in the directory where I launched the agent (because it forgot my instruction not to touch it). That was less surprising and obviously caused by my own setup. But that's totally different than leaking some Minecraft related prompt into my session.
