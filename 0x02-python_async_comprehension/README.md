*** PEP 530 – Asynchronous Comprehensions ***
### Abstract
PEP 492 and PEP 525 introduce support for native coroutines and asynchronous generators using async / await syntax. This PEP proposes to add asynchronous versions of list, set, dict comprehensions and generator expressions.

### Rationale and Goals
Python has extensive support for synchronous comprehensions, allowing to produce lists, dicts, and sets with a simple and concise syntax. We propose implementing similar syntactic constructions for the asynchronous code.

To illustrate the readability improvement, consider the following example:

result = []
async for i in aiter():
    if i % 2:
        result.append(i)
With the proposed asynchronous comprehensions syntax, the above code becomes as short as:

result = [i async for i in aiter() if i % 2]
The PEP also makes it possible to use the await expressions in all kinds of comprehensions:

result = [await fun() for fun in funcs]
Specification
### Asynchronous Comprehensions
We propose to allow using async for inside list, set and dict comprehensions. Pending PEP 525 approval, we can also allow creation of asynchronous generator expressions.

Examples:

set comprehension: {i async for i in agen()};
list comprehension: [i async for i in agen()];
dict comprehension: {i: i ** 2 async for i in agen()};
generator expression: (i ** 2 async for i in agen()).
It is allowed to use async for along with if and for clauses in asynchronous comprehensions and generator expressions:

dataset = {data for line in aiter()
                async for data in line
                if check(data)}
Asynchronous comprehensions are only allowed inside an async def function.

In principle, asynchronous generator expressions are allowed in any context. However, in Python 3.6, due to async and await soft-keyword status, asynchronous generator expressions are only allowed in an async def function. Once async and await become reserved keywords in Python 3.7, this restriction will be removed.

### await in Comprehensions
We propose to allow the use of await expressions in both asynchronous and synchronous comprehensions:

result = [await fun() for fun in funcs]
result = {await fun() for fun in funcs}
result = {fun: await fun() for fun in funcs}

result = [await fun() for fun in funcs if await smth]
result = {await fun() for fun in funcs if await smth}
result = {fun: await fun() for fun in funcs if await smth}

result = [await fun() async for fun in funcs]
result = {await fun() async for fun in funcs}
result = {fun: await fun() async for fun in funcs}

result = [await fun() async for fun in funcs if await smth]
result = {await fun() async for fun in funcs if await smth}
result = {fun: await fun() async for fun in funcs if await smth}
This is only valid in async def function body.
