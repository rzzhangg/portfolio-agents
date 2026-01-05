#!/usr/bin/env python3
"""
WebSearchAPI.ai Search Script
Usage: python search.py "your search query" [--num-results 10] [--freshness day]
"""
 
import argparse
import json
import os
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
 
def search(query: str, num_results: int = 10, freshness: str = None,
           include_content: bool = False, country: str = "US") -> dict:
    """Perform web search using WebSearchAPI.ai"""
 
    api_key = os.environ.get("WEBSEARCHAPI_KEY")
    if not api_key:
        return {"error": "WEBSEARCHAPI_KEY environment variable not set"}
 
    payload = {
        "query": query,
        "num_results": num_results,
        "country": country
    }
 
    if freshness:
        payload["freshness"] = freshness
    if include_content:
        payload["include_content"] = True
 
    data = json.dumps(payload).encode("utf-8")
 
    req = Request(
        "https://api.websearchapi.ai/v1/search",
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        method="POST"
    )
 
    try:
        with urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as e:
        return {"error": f"HTTP {e.code}: {e.reason}"}
    except URLError as e:
        return {"error": f"URL Error: {e.reason}"}
    except Exception as e:
        return {"error": str(e)}
 
def main():
    parser = argparse.ArgumentParser(description="Search the web using WebSearchAPI.ai")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--num-results", type=int, default=10, help="Number of results")
    parser.add_argument("--freshness", choices=["day", "week", "month", "year"],
                        help="Time filter")
    parser.add_argument("--include-content", action="store_true",
                        help="Include full content")
    parser.add_argument("--country", default="US", help="Country code")
 
    args = parser.parse_args()
 
    results = search(
        query=args.query,
        num_results=args.num_results,
        freshness=args.freshness,
        include_content=args.include_content,
        country=args.country
    )
 
    print(json.dumps(results, indent=2))
 
if __name__ == "__main__":
    main()