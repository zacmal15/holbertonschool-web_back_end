export default class Airport {
    constructor(name, code) {
        this._name;
        this._code;
    }

    get [Symbol.toStringTag]() {
        return this._code;
    }
}
