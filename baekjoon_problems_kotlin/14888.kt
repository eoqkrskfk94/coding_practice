import java.util.LinkedList

var minAnswer = Int.MAX_VALUE
var maxAnswer = Int.MIN_VALUE

fun main() {

    val br = System.`in`.bufferedReader()
    val numListCount = br.readLine()
    val numList = br.readLine().split(" ").map { it.toInt() }
    var signs = br.readLine().split(" ").map { it.toInt() }.toMutableList()

    dfs(numList, signs, 1, numList[0])

    println(maxAnswer)
    println(minAnswer)
}

fun dfs(numList: List<Int>,signs: MutableList<Int>, order: Int , answer: Int) {

    if(order == numList.size ) {
        if(answer > maxAnswer) maxAnswer = answer
        if(answer < minAnswer) minAnswer = answer
        return
    }

    for(i in 0 until 4) {
        if(signs[i] == 0) continue

        signs[i]--

        when(i) {
            0 -> {
                dfs(numList, signs, order + 1, answer + numList[order])
            }
            1 -> {
                dfs(numList, signs, order + 1, answer - numList[order])
            }
            2 -> {
                dfs(numList, signs, order + 1, answer * numList[order])
            }
            3 -> {
                if(answer > 0) dfs(numList, signs, order + 1, answer / numList[order])
                else dfs(numList, signs, order + 1, -(-answer / numList[order]))
            }
        }

        signs[i]++

    }

}





