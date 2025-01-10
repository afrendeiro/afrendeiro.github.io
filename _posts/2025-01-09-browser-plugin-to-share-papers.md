---
layout: post
title: "A browser extension for paper sharing in the lab"
description: "A browser extension for paper sharing in the lab"
category: notebook
tags: [workflows, papers, javascript]
---
{% include JB/setup %}


In the Rendeiro Lab, we often come across many papers, blog posts, or useful resources online that we want to share quickly with the team.
While sharing URLs via email isn’t new, I realized there’s always a little friction: copying the title, cleaning it up, grabbing the link, and then opening an email client to put it all together.
It’s not hard—but when you do it often enough, it becomes a chore.

So of course I made a Chrome extension to help.

## What does it do?

SendPaper is a lightweight Chrome extension that simplifies sharing webpage titles and URLs. With just one click, it opens your default email client, pre-filling the subject with a clean title (removing unnecessary clutter like anything after a `|`) and the body with the title and URL separated by a newline.

## Why build this?

We like workflows that keep us focused on research instead of repetitive tasks.
SendPaper integrates seamlessly with the tools we already use—no need for additional apps or services.

## What’s under the hood?

For the tech-savvy, here’s a highlight reel of the features:

- Email address obfuscation using base64 encoding for added security.
- Dynamic title cleaning to strip irrelevant details (everything after `|`).
- Encoded email links to ensure compatibility with all email clients.

The code is [open-source](https://github.com/rendeirolab/sendpaper-chrome-extension), so feel free to adapt it to your needs or contribute improvements.

## What’s next?

I'm thinking of additional features, like pulling metadata from the page (e.g., publication dates).
For now, we’re keeping it simple and functional.

## Try it out!

Give it a spin and see how it fits into your workflow. Feedback is always welcome, so let us know how we can improve it.

Happy sharing!
