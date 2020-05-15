# A open source URL hashing system
A smart and simple URL Shortener

## Choosing System Design 
```
While working around the architecture of the URL Shorten system I was broadly left with below mentioned approaches:
  1. Generating random short urls and saving it along the original one directly to DB.( It involves lots of get and put requests)
  
  2. Using a hashing function( Decently high chances of encountering collision )
      Example:
          MD5( hashing function ) which generates 128-bit hash value

  3. Maintaining a counter approach
      Though counter maintaining approaches can be implgit push -u origin masteremented in multiple ways but the most durable and scalable approach to the best of my knowledge is the Range based method.
      
      In Range based method we allocate a particular range of combinations say 0-1billion which can be further subdivided and use them to generate short urls until we consume that range of combination and then we can other allocate other left combination like 1B-2B(can be maintained in zookeeper or DB) and so on.

```

### Table Schema
```
key-> short url
value-> longer url(original)
```
