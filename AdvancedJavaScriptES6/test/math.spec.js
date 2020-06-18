const assert = require('assert');
const Math = require('../src/math.js');

describe('Math  class', function() {
  it('Sum two numbers', function(done) {
    const math = new Math();
    this.timeout(3000);
    math.sum(5,5, (value) => {
      assert.equal(value, 10);
      done();
    })   
  });
});