# VSM (Vector Space Model)

## Reviews

<details>
    <summary>Boolean Model</summary>
    
* Pros
* Cons
</details>

<details>
    <summary>Probabilistic Model</summary>
    
  * Pros
  * Cons
</details>

<details>
    <summary>Overlap Score Model</summary>
    
  * Pros
  * Cons
</details>
<br/>

## Vector Space Model
<!-- object: -->
* calculated **`TF-IDF`** weighting between query and documents.

* Ranking function follows **`cosine similarity`** :

$$ sim(q,d_{j} )=cos(\theta)=\frac{\vec{q} \cdot \vec{d_{j}}} {|\vec{q}||\vec{d_{j}}|}=\frac{ \color{lime}\overbrace{ \color{silver}\sum_{w_{i}\in{V}} w_{i,q} \times w_{i,j}}^{\text{inner product}}  } {\sqrt{\sum_{w_{i}\in{V}}w^{2}_{i,q} }  \text{ } \color{red}\underbrace{\color{silver}\sqrt{\sum_{w_{i}\in_{V}}w^{2}_{i,j}}}_{\text{vector length}}  } $$

* **Why `cosine similarity` measure instead of `Euclidean distance` measure ?**
    
        The Euclidean distance measure does not consider the different vector lengths of queries and documents.

* Pros
    + improve the quality of the answer set with `TF-IDF`
    + allow partial matching  
    + document length normalization

* Cons
  + It assumes independence of index terms.