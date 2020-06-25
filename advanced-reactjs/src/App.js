import React, {Component} from 'react';

class Twitter extends Component {
  componentWillMount() {
    console.log('componentWillMount')
  }
  componentDidMount() {
    console.log('componentDidMount')
  }
  render () {
    const posts = [{
      title: 'xpto',
      description: 'foo'
    }]
    return (
      <div>
        {this.state.posts}
      </div>
    )
  }
}

export default Twitter