fun main() {
    removeKdigits("1432219", 3)
}

fun removeKdigits(num: String, k: Int): String? {
    if (num.length == k) return "0"
    val sb = StringBuilder(num)

    /*We will iterate the number k times. In each iteration:
        1. Remove the digit for which the next digit is smaller.
        2. If we reach at the end than remove last digit.*/for (j in 0 until k) {
        var i = 0
        while (i < sb.length - 1 && sb[i] <= sb[i + 1]) {
            i++
        }
        sb.delete(i, i + 1)
    }

    //remove leading 0's
    while (sb.length > 1 && sb[0] == '0') sb.delete(0, 1)
    return if (sb.length == 0) {
        "0"
    } else sb.toString()
}

