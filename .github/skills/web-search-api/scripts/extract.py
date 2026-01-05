#!/usr/bin/env python3
"""
WebSearchAPI.ai Content Extraction Script
Usage: python extract.py "https://example.com/article" [--format markdown]
"""
 
import argparse
import json
import os
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
 
def extract(url: str, output_format: str = "markdown",
            include_images: bool = False, clean_content: bool = True) -> dict:
    """Extract content from URL using WebSearchAPI.ai"""
 
    api_key = os.environ.get("WEBSEARCHAPI_KEY")
    if not api_key:
        return {"error": "WEBSEARCHAPI_KEY environment variable not set"}
 
    payload = {
        "url": url,
        "output_format": output_format,
        "include_images": include_images,
        "clean_content": clean_content
    }
 
    data = json.dumps(payload).encode("utf-8")
 
    req = Request(
        "https://api.websearchapi.ai/v1/extract",
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        method="POST"
    )
 
    try:
        with urlopen(req, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as e:
        return {"error": f"HTTP {e.code}: {e.reason}"}
    except URLError as e:
        return {"error": f"URL Error: {e.reason}"}
    except Exception as e:
        return {"error": str(e)}
 
def main():
    parser = argparse.ArgumentParser(description="Extract content using WebSearchAPI.ai")
    parser.add_argument("url", help="URL to extract content from")
    parser.add_argument("--format", choices=["markdown", "text", "html"],
                        default="markdown", help="Output format")
    parser.add_argument("--include-images", action="store_true",
                        help="Include images in output")
    parser.add_argument("--raw", action="store_true",
                        help="Don't clean content")
 
    args = parser.parse_args()
 
    results = extract(
        url=args.url,
        output_format=args.format,
        include_images=args.include_images,
        clean_content=not args.raw
    )
 
    print(json.dumps(results, indent=2))
 
if __name__ == "__main__":
    main()