import kotlin.math.max

fun main(args: Array<String>) {
    val br = System.`in`.bufferedReader()

    var sugarWeight = br.readLine().toInt()
    var bagCount = 0

    while (sugarWeight > 0) {

        if(sugarWeight < 3 || sugarWeight == 4) {
            bagCount = -1
            break
        }

        if(sugarWeight % 5 == 0) {
            bagCount += sugarWeight / 5
            break
        } else {
            sugarWeight -= 3
            bagCount++
        }

    }

    println(bagCount)

}






