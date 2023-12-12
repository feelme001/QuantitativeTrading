# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])

dates = pd.date_range("20130101", periods=6)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)

s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))


                                                       


print("\n##### bject creation #####\n")
print(s)
print("\n##########\n")
print(dates)
print("\n##########\n")
print(df)
print("\n##########\n")
print(df2)
print("\n##########\n")
print(df2.dtypes)
print("\n##########\n")
print(df2.A)
print("\n##### Viewing data #####\n")
print(df2)
print(df2.head(1))
print(df2.tail(3))
print(df)
print(df.index)
print(df.columns)
print(df.to_numpy())
print(df2.dtypes)
print(df2.to_numpy())
print(df.describe())
print(df.T)
print(df.sort_index(axis=1, ascending=False))
print(df.sort_values(by="B"))
print("\n##### Selection #####\n")
print(df["A"])
print(df[0:3])
print(df.iloc[[1, 2, 4], [0, 2]])
print(df.iat[1, 1])
print(df[df > 0])
print(df)
print(s1)
print(df)
df["F"] = s1
print(df)




