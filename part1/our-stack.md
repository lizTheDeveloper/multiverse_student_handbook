# Our Stack: What The Multiverse School Actually Runs

This is the software the school and Multiverse Campus run on today. Campus agents run on it too. When an agent asks you to build something, or you pick a tool for a class project, start here. Something built on our stack can be plugged into the school; something built on a stack we don't run usually can't.

You can use other tools when a class is comparing frameworks, or when you have a real reason. Say why in your README.

Each section below covers one kind of job.

## Our stack: language models

- **Campus agents think with Qwen 3.8 27B**, an open-weight model, called through **OpenRouter**. Every agent you talk to on campus runs on it.
- **Claude** (Opus 5.5, Sonnet 5.5, Haiku 5.5) handles the heavy reasoning: drafting, reviewing and hard judgment calls. It's called through OpenRouter or the Anthropic API.
- **Running a model on your own machine:** use LM Studio (or Ollama) with a Qwen model. Both serve an OpenAI-compatible API, so code written against OpenRouter works locally by changing the base URL.
- **Call models through the OpenAI-compatible chat completions API.** It's a protocol, and OpenRouter, LM Studio and Ollama all speak it. That doesn't mean using OpenAI's models.
- **We don't build on GPT-4o, ChatGPT or OpenAI-hosted models.** If an older lesson uses them, swap in a Qwen model through OpenRouter or LM Studio.

## Our stack: building agents

- **Claude Code** is how we build software at the school, from writing code to reviewing and testing it.
- **An agent is a loop:** a model, a list of tools, and code that runs the tool calls the model asks for. Write it yourself against the chat completions API, or use the **Claude Agent SDK** (Python or TypeScript).
- **Tools are MCP servers.** We write them in Python with **FastMCP**, run with **uv**, or in TypeScript with the official MCP SDK. One MCP server can be used by Claude Code, Claude Desktop and campus agents alike.
- **Agents talk to each other over NATS** (agent-to-agent messages and events).
- **Agents talk to people on Matrix**, the school's chat (matrix.themultiverse.school), and on Multiverse Campus.
- Frameworks like LangGraph, CrewAI, AutoGen or smolagents are fine for comparing approaches in class. Deliverables for the school should be plain loops, the Claude Agent SDK, or MCP.

## Our stack: memory, search and RAG

- **PostgreSQL 16 with pgvector** holds everything, embeddings included. We don't use a separate vector database (no Pinecone, Chroma or Weaviate).
- **Embeddings come from qwen3-embedding-8b, stored as 1024-dimension vectors**, compared with cosine distance (`<=>` in pgvector).
- Split documents on their headings (`#`, `##`, `###`) into sections of about 2,000 characters, store each with its title and a link back to the source, and re-embed only what changed.
- **Campus agents remember things in tiers:** short-term conversation, facts about a player, and shared knowledge. They search this handbook, the Akashic Library and class recordings the same way.
- For a small project on your laptop, SQLite or a plain JSON file is fine. Say so in your README.

## Our stack: apps, data and jobs

- **Python:** Flask, psycopg2 (plain SQL, no ORM), managed with **uv**. This is the school website.
- **TypeScript:** Node 20, Express, Socket.IO, React and Vite. This is Multiverse Campus.
- **Background jobs:** pg-boss (on Postgres) for campus, and a Python job runner with APScheduler for the school.
- **Redis** for sessions and short-lived state.
- **Live voice and video:** LiveKit.
- **Analytics:** Umami. No tracking pixels.

## Our stack: testing, watching and shipping

- **Tests:** pytest for Python, Vitest for TypeScript, **Playwright** for anything in a browser. Take a screenshot to prove a page works.
- **Watching agents:** every model call goes to **Langfuse**, labelled with the app and what it was doing. Errors go to **GlitchTip** (Sentry-compatible).
- **Shipping:** Docker images, deployed with Coolify on one server that runs on renewable power, with Cloudflare in front. CI runs on our own server, not GitHub Actions.
- **Delivering your work:** a public GitHub repo, a public page (GitHub Pages is fine), or a doc. Whoever you built it for has to be able to open it without an account.

## Our stack: quick swaps for older lessons

Some older lessons and exercises name tools we've moved off. Swap them like this:

| If the lesson says | Use |
|---|---|
| OpenAI API, GPT-4o, GPT-4, ChatGPT | Qwen through OpenRouter (or LM Studio locally); Claude for heavy reasoning |
| OpenAI embeddings | qwen3-embedding-8b, 1024 dimensions |
| Pinecone, Chroma, FAISS, Weaviate | PostgreSQL + pgvector |
| LangChain or LlamaIndex pipelines | A plain loop, the Claude Agent SDK, or MCP tools |
| Discord or Slack bots | Matrix (matrix.themultiverse.school) |
| pip install into your system Python | uv |
| GitHub Actions | Tests you run yourself; say how in the README |
| Google Analytics, tracking pixels | Umami |
