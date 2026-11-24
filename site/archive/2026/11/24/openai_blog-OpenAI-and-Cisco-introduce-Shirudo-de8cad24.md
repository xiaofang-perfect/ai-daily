---
title: "OpenAI and Cisco introduce Shirudo"
source: OpenAI
url: https://openai.com/index/introducing-shirudo
date: 2026-11-24
published_at: 2026-11-23T21:20:00+00:00
tag: 工具开源
item_id: de8cad2433b13a0d
---
# OpenAI and Cisco introduce Shirudo

An open-source runtime that helps operators protect running Linux systems without needing to wait for the patch or restarts

![Shirudo logo on an orange gradient background.](https://images.ctfassets.net/kftzwdyauwt9/5K7gFDr3r8vgjdIcsW6RVY/aba5325ce7902e5d1499b907f8e78f0b/shirudo-partner-logos-landscape-2x.png?w=3840&q=90&fm=webp)

OpenAI and Cisco are launching Shirudo, an open-source runtime that helps teams protect Linux systems while they roll out patches. In a [<u>controlled test</u>(opens in a new window)](https://isovalent.com/blog/post/cisco-openai-shirudo/), a Codex-generated shield blocked a Java4Shell exploit attempt against a running Elasticsearch service without requiring a restart.

We’re inviting developers, security researchers, and infrastructure operators across the industry to help develop the project further. The project brings together OpenAI’s frontier AI, security and infrastructure research and Cisco’s infrastructure and security expertise to help protect the systems people rely on every day.

Testing and deploying a patch can still take days or weeks. Protecting a service in the meantime can be challenging because an exploit and a legitimate request may rely on the same Linux operation. Blocking that operation entirely could take the service offline.

Shirudo (Japanese for “shield”) is designed to help security teams navigate this tradeoff. Teams can test whether a temporary safeguard, called a shield, blocks the behavior that exposes a vulnerability while allowing legitimate requests through. Once an operator approves the shield, it can be deployed while the service continues running.

Shirudo uses eBPF, a Linux technology that allows small programs to run at specific points inside the operating system. This makes it possible to observe suspicious activity and apply targeted security protections to running systems.

![The guardian agent uses eBPF instruments to observe kernel and network activity and eBPF controls to apply targeted protections.](https://images.ctfassets.net/kftzwdyauwt9/bScTLq9smNJq5XAlaHIQW/fab0e70b1aab8ca8dffb70a747056fd7/guardian-agent-desktop-light.png?w=3840&q=90&fm=webp)

How the guardian agent observes and protects a running system with eBPF.

OpenAI and Cisco are designing Shirudo around four core capabilities:

- **Live protection:** eBPF shields can block vulnerable code paths without restarting the system. Security teams can monitor how a proposed shield would affect applications before enforcing it.
- **Defense at machine speed:** OpenAI and Cisco are designing Shirudo to give agents programmable controls to investigate vulnerabilities, develop targeted shields, and validate their effectiveness against exploits and real workloads. Security teams control what gets deployed.
- **Trusted deployment:** Shields are cryptographically signed and verified before loading. Linux's eBPF verifier checks eBPF programs against its safety rules, while kernel security controls restrict unauthorized changes.
- **Hardware-backed verification:** Shirudo uses a Trusted Platform Module (TPM) to support a verifiable record of protections being loaded or removed. Operators can use this evidence to check whether systems meet their security requirements.

The [<u>Shirudo technical walkthrough</u>(opens in a new window)](https://lpc.events/event/20/contributions/2437/) from the Linux Plumbers Conference shows how to [<u>apply a shield and verify it on the target host</u>(opens in a new window)](https://www.youtube.com/watch?v=4v2xA_NJHt0). The Java4Shell vulnerability is another example illustrating how a targeted shield can protect a running application while a permanent patch is being prepared. Using OpenAI's Codex, the team generated a shield that added an input check to Java's Base64 decoder and attached it directly to a running Elasticsearch process. When attempting to exploit the vulnerability, the shield rejected the malicious input, blocking the attack while Elasticsearch continued running. You can read more [<u>here</u>(opens in a new window)](https://isovalent.com/blog/post/cisco-openai-shirudo/).

Shirudo is a first step toward infrastructure that can adapt to emerging threats while remaining reliable. We want to strengthen the operating system foundations needed to deploy these protections at scale, including hardening the kernel and core services, limiting workload permissions, and making updates and recovery safer.

Our long-term goal is to enable defenders and AI agents to quickly identify affected systems, validate protections, and deploy eBPF shields that block exploits without disrupting workloads. Applications should run with only the permissions they need, governed by policies that are automatically generated and maintained.

We will combine frontier AI with security and infrastructure research to discover vulnerabilities and test defenses against realistic attacks. We aim to make it easier for operators to detect and contain compromises, prevent attackers from moving across systems, and restore services to a verified, known-good state. Hardware-backed attestation and independent network controls provide additional assurance even if individual systems are compromised.

OpenAI and Cisco are open-sourcing [<u>Shirudo</u>(opens in a new window)](https://github.com/shirudo-dev/shirudo) so developers, security researchers, and infrastructure operators can inspect the code, test protections, and contribute to its development. Shirudo is licensed under BSD 2-Clause, with its BPF programs dual-licensed under BSD and GPL.

Our goal is to make tested shields available alongside vulnerability disclosures, giving operators a way to evaluate and deploy temporary protections while preparing permanent patches.

- **Try Shirudo:** Follow the [<u>VM quickstart</u>(opens in a new window)](https://docs.shirudo.dev/start/quickstart.html) to sign, load, and verify a test protection.
- **Get hands-on:** Explore Shirudo through [<u>Isovalent's self-guided lab</u>(opens in a new window)](https://labs.isovalent.com/#/lab/shirudo-getting-started).
- **Join the technical deep dive:** Register for the [<u>December 15 webinar</u>(opens in a new window)](https://isovalent.site/4t8Pjxc).

We’re building Shirudo in the open with the people who build, run, and secure Linux systems. We welcome contributions to the runtime, new shields, and improvements to Linux and eBPF. If you'd like to get involved, take a look at the [<u>code on GitHub</u>(opens in a new window)](https://github.com/shirudo-dev/shirudo), read the [<u>docs</u>(opens in a new window)](https://docs.shirudo.dev/index.html), and [<u>let us know what you find</u>(opens in a new window)](https://docs.shirudo.dev/contribute/support.html).

## Author

## Keep reading

[View all](https://openai.com/news/)
