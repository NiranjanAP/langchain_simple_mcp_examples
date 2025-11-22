# langchain_simple_mcp_examples

This repository contains simple examples demonstrating a minimal MCP-style server and client using langchain-style tools. The examples are intentionally small and easy to run from the terminal so you can learn how an MCP-like tool server and client interact.

Files
- math_server.py — a minimal MCP server that exposes two tools: `add` and `square`.
- clientfor_math_server.py — a client that demonstrates calling the tools on `math_server.py` and printing results to stdout.
- weather_server.py — a small server that exposes tools to fetch weather data from the National Weather Service (https://api.weather.gov). The server adds the required User-Agent header and includes simple caching.
- clientfor_weather_server.py — a client that demonstrates calling the weather tools on `weather_server.py` (or directly testing the weather endpoints) and printing results to stdout or using them in an example flow.
- clientfor_websearch.py — a small example client demonstrating direct web search or lightweight retrieval to retrieve page titles/snippets for a query. This example is intended for learning/demo purposes; follow applicable terms of service and robots.txt when running web requests.

Quick overview
- math_server.py implements two basic tools:
  - add(a, b): returns a + b
  - square(x): returns x * x
- clientfor_math_server.py connects to the server and demonstrates invoking those tools. Both scripts are runnable from a terminal and meant for local testing and learning.

- weather_server.py implements tools that contact the National Weather Service API (https://api.weather.gov) to retrieve forecast data for a given latitude/longitude. The server ensures a descriptive User-Agent header is sent (required by NWS) and performs lightweight in-memory caching to avoid frequent repeat requests.
- clientfor_weather_server.py is a small Python client to test the weather tools and demonstrates retrieving forecasts for sample coordinates.

- clientfor_websearch.py demonstrates a basic direct web search/retrieval approach: it can call a public search endpoint or fetch a small set of web pages and extract titles and short snippets. It is intended as an example of integrating retrieval into an MCP-style setup; if you plan to run automated searches at scale, prefer using a search API and follow rate limits and usage policies.

Prerequisites
- Python 3.8+ (or any supported Python 3 version)
- requests (used by several examples)
- For the web search example, optional dependencies may include beautifulsoup4 for HTML parsing; if a search API is used you'll need its client or API key.

How to run (basic)
1. Start the math server (example)
```bash
python math_server.py
```
This will start the simple MCP server on the configured host/port (see the top of `math_server.py` for host/port settings).

2. In another terminal, run the math client
```bash
python clientfor_math_server.py
```
The client should call the exposed tools and print results to stdout.

3. Start the weather server
```bash
python weather_server.py
```
This will start the weather MCP-style server that exposes weather-related tools. The server will contact api.weather.gov when asked for a forecast for the provided coordinates.

4. In another terminal, run the weather client
```bash
python clientfor_weather_server.py
```
This client demonstrates calling the weather tools and printing a human-readable summary of the returned forecast data.

5. Run the web search example client
```bash
python clientfor_websearch.py
```
Depending on the implementation, the script will either query a search API or fetch a small set of pages and print titles/snippets for the top results.

Example expected output (client)
```text
Calling add(2, 3) -> 5
Calling square(4) -> 16

# Weather client sample output (actual content will vary based on coordinates and the upstream API):
Fetching forecast for 38.8977, -77.0365
Forecast for Washington, DC area:
- Tonight: Clear, Low 45°F
- Monday: Sunny, High 68°F

# Web search example (sample output):
Query: "python web scraping"
Results:
1) "Web Scraping with Python — Tutorial" — A short snippet or summary...
2) "Beautiful Soup: Documentation" — A short snippet or summary...
```
(Exact output will depend on the example implementations in the client files and the live data.)

Troubleshooting
- ImportError: If running any script raises ImportError for a package such as `requests` or `beautifulsoup4`, install the missing package via pip. Example:
```bash
pip install requests beautifulsoup4
```
- NWS API requirements: the National Weather Service requires requests to include a descriptive User-Agent header with contact information. If you see upstream errors or 403 responses, ensure `weather_server.py` sets a User-Agent with a valid contact email or URL.
- Web search/scraping etiquette: follow robots.txt and the target site's terms of service. If you get blocked or rate-limited, reduce request frequency, add delays, or switch to an official API.
- Port/address in use: if the server fails to bind because the port is already used, either stop the process using that port or change the port in the server file.

Suggested next steps
- Add a requirements.txt if you want reproducible installs.
- Add more example tools (e.g., multiply, divide) and expand the client to demonstrate error handling and timeouts.
- For the weather example:
  - Add a small frontend (Flask or static HTML + JS) that displays the forecast in a browser.
  - Add geocoding (city-name search) so users can enter a place name instead of coordinates.
  - Replace the in-memory cache with Redis for production use.
- For the web search example:
  - Add an optional adapter to call a search API (Bing, Google, or other) for more reliable results.
  - Add rate limiting and retry/backoff logic.

License
MIT
