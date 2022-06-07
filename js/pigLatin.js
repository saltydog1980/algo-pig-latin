exports.translate = function(word) {
    vowelList = ['a', 'e', 'i', 'o', 'u',];
    answer = ""
    wordArr = word.split(' ')
    if (wordArr.length === 1) {
        oneWord = wordArr.join('')
        if (vowelList.includes(word[0])){
            answer = word + 'ay'
        } else {
            array =  word.split('')
            while (!vowelList.includes(array[0])) {
                if (array[0] === 'q' && array[1] === 'u') {
                    temp = array.slice(0, 2)
                    array.push(temp[0])
                    array.push(temp[1])
                    array.shift()
                    array.shift()
                } else {
                    temp = array.shift()
                    array.push(temp)
                }
            }
            answer = array.join('') + 'ay'
        }
    } else {
        let ans = []
        wordArr.map(element => {
            if (vowelList.includes(element[0])){
                ans.push(element + 'ay')
            } else {
                array =  element.split('')
                while (!vowelList.includes(array[0])) {
                    if (array[0] === 'q' && array[1] === 'u') {
                        temp = array.slice(0, 2)
                        array.push(temp[0])
                        array.push(temp[1])
                        array.shift()
                        array.shift()
                    }else {
                        temp = array.shift()
                        array.push(temp)
                    }
                    
                }
                ans.push(array.join('') + 'ay')
            }
            
        })
        answer = ans.join(' ')
    }
    return answer
};
 
