# First Principles

The point of this skill is not to memorize pages. The point is to reduce Agiso integration work into a stable model that survives service differences and incomplete docs.

## Core Object Model

Every Agiso integration can be understood as:

1. **A namespace**
   Example: `alds`, `acs`, `open`, `print`, `supplier`
2. **A credential boundary**
   Example: AppId and AppSecret for platform APIs, clientId and clientSecret for supplier flows, token for merchant authorization
3. **A canonical request**
   Endpoint path, HTTP method, parameter set, and gateway base URL
4. **A signature rule**
   Sort params, concatenate key-value pairs, wrap with secret, MD5
5. **A response contract**
   Success bit plus structured failure details
6. **An optional asynchronous edge**
   Push notifications and supplier-side callbacks

If an answer does not clarify one of these, it is likely not solving the real problem.

## Why This Repository Fits A Skill

This repository already contains:

- domain-specific knowledge that a general model does not reliably know
- repeated service structure across 15 services
- extracted indexes from reverse-engineered frontend assets
- code and prose examples that can be turned into reliable generation patterns

This makes it a strong skill candidate because the reusable value is procedural and domain-bound, not generic.

## Decision Order

When solving a user request, decide in this order:

1. Which service owns the task?
2. Which identity or auth flow is required?
3. Is the user asking for a read path, write path, callback path, or supplier path?
4. Which canonical docs are required?
5. Which parts are documented, and which parts must be inferred from extracted artifacts?

## Failure Modes

The most common ways to go wrong are:

- choosing the wrong service variant
- treating a marketplace-specific `alds*` variant as interchangeable with another
- getting signature parameter order wrong
- omitting auth context from generated code
- ignoring the Agiso response envelope
- assuming scraped docs are complete or current

## What A Good Output Looks Like

A good Agiso-skill output usually includes:

- the selected service and why it was selected
- the relevant source documents
- the exact endpoint or callback topic
- the signing rule and required parameters
- a runnable example or implementation stub
- explicit uncertainty where docs are incomplete
