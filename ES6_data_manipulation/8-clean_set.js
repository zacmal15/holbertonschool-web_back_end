export default function cleanSet(set, startString) {
    if (type of startString !== 'string' || startString === '') {
        return '';
    }

    return [...set]
        .filter((value) => value.startsWith(startString))
        .map((value) => value.slice(startString.length))
        .join('-');
}
