# Portfolio Management AI Agents and Tools

Sets of AI agents and their associated tools specialize in managing investment portfolio.

## Investment Portfolio

The investment portfolio could have the assets of,
- bank chequing, saving, GIC accounts
- bank mortgage accounts
- discount brokerage investment accounts, including registered investment accounts
- life insurance accounts
- employee investment accounts
- real estate condo units
- other asset types

## Portfolio Goals

The portfolio should generate a stable annual cash income of $150,000.00 Canadian Dollars as the retirement income for a couple without the need of withdrawing from the capital. It's main an income oriented investment portfilo, where capital must be preserved.

Equity investment in the portfolio should carry an overall risk below the average market risk level. Stocks selected in the portfolio must be the businesses which is sustainable and continuously generating income in long term.

## Capabilities of AI Agents and Tools

### Bad investment decisions and lessons learned as the context and examples for agents

Bad investment decisions and lessons learned must be built into custom agents' MD files for LLMs to perform its and analysis to make more sound decisions.

How to improve

- [Improvement = Pain + Reflection + Write the lessons into Custom Agents](pain-reflection-improvement.png)

- Build instructions of the agents from the experiences shared in 
    - [Don't be fooled by the "peaceful and quiet" facade: Bridgewater CIO Greg Jensen](https://www.youtube.com/watch?v=swjMP4NEE88)
    - [Greg Jensen - Co-CIO of Bridgewater, Podcast, In Good Company](https://www.youtube.com/watch?v=zRkNO9yNYoI)

- 


### Cash flow monitoring and analysis

- Ingest banking account balances and transactions from the account PDF statements
- Build up monthly cash flow based on transaction activities in banking accounts
- Predict spending and recommend for spending control

### Stock analysis

- Deep holistic research of the holding or targeting stocks for buying or selling the stocks. Research materials include financial reports, analyst researchs, company events and announcements, stock price trends, etc.

### Real estate condo unit management

- Monitor rental market trend for the condo unit, where the rents of all the similar rental units around the location of the condo unit are tracked and analyzed

### Canadian Telcom stocks

- Critical thinking over investment assumptions with Canadian Telcom stocks

## Skills

### Web Search API skill

- Leverage websearchapi.ai for web search

## Security Requirements

- Data protection is the number one requirement for AI agents and their tools. Sensitive information of the banking accounts and the investment accounts should be strictly protected.

### Critical: Authentication & Security Credentials

- PINs (Personal Identification Numbers): Used for ATM/Card transactions.
- Passwords / Biometric Data: Used for online banking login.
- CVV/CVC Codes (Card Verification Values): The 3 or 4 digits on the back of a card.
- MFA Tokens / OTPs: One-time passwords for verification.

### Highly Sensitive: Financial Identifiers

- PAN (Primary Account Number): The 16-digit credit/debit card number.
- Bank Account Number: The core identifier for a checking or savings account.
- IBAN / Routing Numbers: While sometimes public (on checks), combined with an account number, they facilitate fraud.

### PII: Personally Identifiable Information 

- SSN (Social Security Number) / National ID: The "keys to the kingdom" for identity theft.
- Date of Birth: Often used as a verification question.
- Full Name & Address: Links the financial data to a person.
- Mother’s Maiden Name: Common legacy security question answer.

## High-level Architecture

Leverage QWen VL model to create architecture diagram in draw.io format from hand draw diagrams

## Tools from MCP Servers

### MCP server for local Ollama

Expose deepseek-ocr in ollama for extract data format from PDFs

- Extract transactions from deposit or credit card account statement from bank
- Convert stock research PDF documents into MD files


## Command line examples

- Canadian Telco Agent
```
copilot --allow-all-tools --allow-all-paths --allow-all-urls --agent canadian-telco --model gemini-3-pro-preview -p 'For building up an income stream for retirement, investing in Bell Canda, a leading Canadian telco company, is a good option due to its stable dividend yield and strong market position in Canadian Telcom industry'
```
