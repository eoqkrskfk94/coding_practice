fun main(args: Array<String>) {
    val br = System.`in`.bufferedReader()

    var (a, b) = br.readLine().split(" ")
    var difference = 0
    if (a.length == b.length) {
        difference = checkLetterDifferenceRate(a, b)
    } else if (b.contains(a)) {
        difference = 0
    } else {
        difference = a.length
        for(i in b.indices) {

            if(b.substring(i).length < a.length) {
                break
            } else {
                val temp = checkLetterDifferenceRate(a , b.substring(i))
                if(difference > temp) {
                    difference = temp
                }
            }
        }

    }


    println(difference)
}

fun checkLetterDifferenceRate(a: String, b: String): Int {
    var difference = 0


    for (i in a.indices) {
        if (a[i] != b[i]) {
            difference += 1
        }
    }

    return difference
}



