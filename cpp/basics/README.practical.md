## 当数组作为参数传递时，它会被转换为指向第一个元素的指针

## indexing
1. vector
vec1[i]
2. VectorXd
vecxd(i)
3. MatrixXd
matxd(i,j)

## erase iterator in for loop

```
for (auto it = m.cbegin(); it != m.cend() /* not hoisted */; /* no increment */)
{
  if (must_delete)
  {
    m.erase(it++);    // or "it = m.erase(it)" since C++11
  }
  else
  {
    ++it;
  }
}
```