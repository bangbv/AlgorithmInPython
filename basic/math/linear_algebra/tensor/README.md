# Matrix vs Tensor Comparison

| Feature            | Matrix                                                         | Tensor                                                                                                               |
|:-------------------|:---------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------|
| **Dimensionality** | Two-dimensional array (rows and columns)                       | Multi-dimensional array (including 0, 1, 2, and higher dimensions)                                                   |
| **Rank/Order**     | Rank 2                                                         | Rank 0 (scalar), 1 (vector), 2 (matrix), 3, ... $n$                                                                  |
| **Transformation** | May or may not explicitly adhere to tensor transformation laws | **Defined** by its specific transformation laws under a change of basis                                              |
| **Generality**     | A specific case of a second-order tensor                       | A more general mathematical object encompassing scalars, vectors, and matrices                                       |
| **Use Cases**      | Linear transformations, data tables, etc.                      | Physics (e.g., stress tensor, metric tensor), machine learning (representing multi-dimensional data), geometry, etc. |