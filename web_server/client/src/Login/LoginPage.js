import React from 'react';
import PropTypes from 'prop-types';
import Auth from '../Auth/Auth';
// PropTypes exports a range of validators that can be used to make sure the data you receive is valid. 

import LoginForm from './LoginForm';

class LoginPage extends React.Component {
    // constructor is the right place to initialize state
    // use super(props) for React.Component subclass, otherwise this.props will be undefined
    constructor(props, context) {
        super(props, context);

        // set the initial component state
        this.state = {
            errors: {},
            user: {
                email: 'xinxinhe1991@gmail.com',
                password: 'hxhx11180103'
            }
        };

        this.processForm = this.processForm.bind(this);
        this.changeUser = this.changeUser.bind(this);
    }

    // Pre-submission handler
    processForm(event) {
        // don't use the default POST submit
        event.preventDefault();

        const email = this.state.user.email;
        const password = this.state.user.password;

        // post login data

        fetch('/auth/login', {
            method: 'POST',
            cache: false,
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                email: email,
                password: password
            })
        }).then(response => {
            if (response.status === 200) {
                this.setState({
                    errors: {}
                });

                response.json().then(function(json) {
                    console.log(json);
                    Auth.authenticateUser(json.token, email);
                    this.context.router.replace('/');
                }.bind(this));
            } else {
                console.log('Login Failed!');
                response.json().then(function(json) {
                    const errors = json.errors ? json.errors : {};
                    errors.summary = json.message;
                    this.setState({errors});
                }.bind(this));
            }
        });
    }

    // trigger when the field changes
    changeUser(event) {
        const field = event.target.name;
        const user = this.state.user;
        user[field] = event.target.value;
       
        // if change email field, user['email'] will be changed
        // if change password field, user['password'] will be changed

        this.setState({user});
    }

    // separate the logic and UI by LoginForm element
    render() {
        return (
            <LoginForm
                onSubmit={this.processForm}
                onChange={this.changeUser}
                errors={this.state.errors}
                user={this.state.user}
            />
        );
    }
}

// To make react-router work
LoginPage.contextTypes = {
    router: PropTypes.object.isRequired
};

export default LoginPage;
