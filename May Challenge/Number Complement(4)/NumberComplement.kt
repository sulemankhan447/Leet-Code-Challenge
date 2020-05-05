class Solution {
    fun findComplement(num: Int): Int {
        val number_of_bits = Math.floor(
            Math.log(num.toDouble()) /
                    Math.log(2.0)
        ).toInt() + 1

        // XOR the given integer with poe(2, 
        // number_of_bits-1 and print the result 
        return (1 shl number_of_bits) - 1 xor num
    }
}
