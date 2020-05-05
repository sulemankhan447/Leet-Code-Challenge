class Solution {
    fun firstUniqChar(s: String): Int {
        val count = HashMap<Char, Int>()
        val n = s.length
        // build hash map : character and how often it appears
        for (i in 0 until n) {
            val c = s[i]
            count[c] = count.getOrDefault(c, 0) + 1
        }

        // find the index
        for (i in 0 until n) {
            if (count[s[i]] === 1) return i
        }
        return -1
    }
}
