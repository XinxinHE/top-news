import React from 'react';
import PropTypes from 'prop-types';
//import Auth from '../Auth/Auth';
// PropTypes exports a range of validators that can be used to make sure the data you receive is valid. 

import SignUpForm from './SignUpForm';

class SignUpPage extends React.Component {
    // constructor is the right place to initialize state
    // use super(props) for React.Component subclass, otherwise this.props will be undefined
    constructor(props) {
        super(props);

        // set the initial component state
        this.state = {
            errors: {},
            user: {
                email: '',
                password: '',
                confirm_password: ''
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
        const confirm_password = this.state.user.confirm_password;        

        if (password !== confirm_password) {
            return;
        }
        // post login data

        fetch('http://localhost:3000/auth/signup', {
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

                this.context.router.replace('/login');
            } else {
                console.log('Signup Failed!');
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
        // if change confirm_password field, user['confirm_password'] will be changed

        this.setState({user});

        if (this.state.user.password !== this.state.user.confirm_password) {
            const errors = this.state.errors;
            errors.password = "Password and Confirm Password don't watch";
            this.setState({errors}); // refresh UI and state
        } else {
            const errors = this.state.errors;
            errors.password = '';
            this.setState({errors});
        }
    }

    // separate the logic and UI by LoginForm element
    render() {
        return (
            <SignUpForm
                onSubmit={this.processForm}
                onChange={this.changeUser}
                errors={this.state.errors}
                user={this.state.user}
            />
        );
    }
}

// To make react-router work
SignUpPage.contextTypes = {
    router: PropTypes.object.isRequired
};

export default SignUpPage;