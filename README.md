# langchain_simple_mcp_examples


This repository contains simple examples demonstrating a minimal MCP-style server and client using langchain-style tools. The examples are intentionally small and easy to run from the terminal so you can see how a server exposes tools and how a client can call them.

Files
- math_server.py — a minimal MCP server that exposes two tools: `add` and `square`.
- clientfor_math_server.py — a client that demonstrates calling the tools on `math_server.py` and printing results.

Quick overview
- math_server.py implements two basic tools:
  - add(a, b): returns a + b
  - square(x): returns x * x
- clientfor_math_server.py connects to the server and demonstrates invoking those tools. Both scripts are runnable from a terminal and meant for local testing and learning.

Prerequisites
- Python 3.8+ (or any supported Python 3 version)
- No additional libraries are strictly required if the example uses only the standard library. If your version of the example uses langchain or other MCP helper packages, install those accordingly (for example `pip install langchain`) — check the top of each file for any import statements that require external packages.

How to run (basic)
1. Start the server
```bash
python math_server.py
```
This will start the simple MCP server on the configured host/port (see the top of `math_server.py` for host/port settings).

2. In another terminal, run the client
```bash
python clientfor_math_server.py
```
The client should call the exposed tools and print results to stdout.

Example expected output (client)
```text
Calling add(2, 3) -> 5
Calling square(4) -> 16
```
(Exact output will depend on the example implementation in `clientfor_math_server.py`.)

Troubleshooting
- ImportError: If running either script raises ImportError for a package such as `langchain` or other MCP helpers, install the missing package via pip. Example:
```bash
pip install langchain
```
- Port/address in use: if the server fails to bind because the port is already used, either stop the process using that port or change the port in `math_server.py`.

Suggested next steps
- Add a requirements.txt if you want reproducible installs (I can create one listing the exact packages used by the scripts).
- Add more example tools (e.g., multiply, divide) and expand the client to demonstrate error handling and timeouts.
- Add unit tests for both server tool implementations and the client calls.
