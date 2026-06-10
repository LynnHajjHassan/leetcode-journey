# Week 1: Arrays + HashMap/HashSet

## Goal

Rebuild confidence with arrays, loops, indexes, HashMap, and HashSet.

## Problems

- [x] Two Sum
- [ ] Contains Duplicate
- [ ] Valid Anagram
- [ ] Group Anagrams
- [ ] Product of Array Except Self or Top K Frequent Elements

---

## Pattern Notes

### HashMap

Use when:
- I need fast lookup
- I need to count frequencies
- I need to remember values I already saw

Common Java syntax:

```java
HashMap<Integer, Integer> map = new HashMap<>();
map.put(key, value);
map.containsKey(key);
map.get(key);
map.getOrDefault(key, 0);
```

### HashSet

Use when:
- I only need to know if something exists
- I do not need to store a value with it

Common Java syntax:

```java
HashSet<Integer> set = new HashSet<>();
set.add(x);
set.contains(x);
```

### Mistakes to Watch For
- Mixing up index and value
- Forgetting duplicates
- Adding to the map too early
- Not checking edge cases