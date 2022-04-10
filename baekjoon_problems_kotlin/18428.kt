import java.util.LinkedList
import kotlin.math.abs

//var map = mutableListOf<MutableList<Int>>()
var wallCandidates = mutableSetOf<List<Pair<Int, Int>>>()

fun main() {

    val br = System.`in`.bufferedReader()
    val n = br.readLine().toInt()

    var map = mutableListOf<MutableList<String>>()

    repeat(n) {
        map.add(br.readLine().split(" ").toMutableList())
    }

    allWallCombinations(map, MutableList(n) { MutableList(n) { false } }, 0, mutableListOf(), n)

    var wallCandidatesList = wallCandidates.toList()


    wallCandidatesList.forEach {
        if(check(map, it, n)) {
            println("YES")
            return
        }
    }


    println("NO")


}

fun allWallCombinations(
    map: MutableList<MutableList<String>>,
    visit: MutableList<MutableList<Boolean>>,
    count: Int,
    comb: MutableList<Pair<Int, Int>>,
    n: Int
) {

    if (count == 3) {
        wallCandidates.add(comb.toList().sortedBy { it.first }.sortedBy { it.second })
        return
    }

    for (i in 0 until n) {
        for (j in 0 until n) {
            if (visit[i][j] == true) continue
            if (map[i][j] == "T" || map[i][j] == "S") continue

            visit[i][j] = true
            comb.add(Pair(i, j))

            allWallCombinations(map, visit, count + 1, comb, n)

            visit[i][j] = false
            comb.removeAt(comb.lastIndex)
        }
    }
}

fun check(map: MutableList<MutableList<String>>, wallCandidate: List<Pair<Int, Int>>, n: Int): Boolean {
    val teachers = mutableListOf<Pair<Int, Int>>()

    var newMap = MutableList(n) { MutableList(n) { "X" } }

    for (i in 0 until wallCandidate.size) {
        newMap[wallCandidate[i].first][wallCandidate[i].second] = "O"
    }

    for (i in 0 until n) {
        for (j in 0 until n) {
            if (map[i][j] == "T") {
                teachers.add(Pair(i, j))
                newMap[i][j] = "T"
            } else if (map[i][j] == "S") {
                newMap[i][j] = "S"
            }

        }
    }

    for (i in 0 until teachers.size) {

//        if(wallCandidate == listOf(Pair(0, 0), Pair(3, 2), Pair(2, 3))) {
//            println(teachers)
//        }

        var leftCheck = teachers[i].second
        while (leftCheck >= 0) {
            if(newMap[teachers[i].first][leftCheck] == "O") break
            if(newMap[teachers[i].first][leftCheck] == "S") return false
            leftCheck--
        }

        var rightCheck = teachers[i].second
        while (rightCheck < n) {
            if(newMap[teachers[i].first][rightCheck] == "O") break
            if(newMap[teachers[i].first][rightCheck] == "S") return false
            rightCheck++
        }

        var topCheck = teachers[i].first
        while (topCheck >= 0) {
            if(newMap[topCheck][teachers[i].second] == "O") break
            if(newMap[topCheck][teachers[i].second] == "S") return false
            topCheck--
        }

        var bottomCheck = teachers[i].first
        while (bottomCheck < n) {
            if(newMap[bottomCheck][teachers[i].second] == "O") break
            if(newMap[bottomCheck][teachers[i].second] == "S") return false
            bottomCheck++
        }

    }


    return true

}









