# Two Sum

Traverse the `nums` and check if `target - element` is in the remaining `nums`

**Note**

* One-pass hash table
    * Use Python's dict to implement
    * Set the `target - element` in hash table during the traversing
    * If further element is in that dict, that's it.
