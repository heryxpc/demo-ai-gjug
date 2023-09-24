package com.example.myspringbootloginapp;

import java.util.List;
import java.util.Optional;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class LoginController {

    private static final Logger logger = LoggerFactory.getLogger(LoginController.class);

    @Autowired
    private UserRepository userRepository;

    @PostMapping("/login")
    public LoginResponse login(@RequestBody LoginRequest loginRequest) {
        Optional<User> user = userRepository.findByUsernameAndPassword(loginRequest.getUsername(), loginRequest.getPassword());
        if (user.isPresent()) {
            logger.info("User {} logged in successfully", loginRequest.getUsername());
            return new LoginResponse(true, "Continue");
        } else {
            logger.warn("User {} not found", loginRequest.getUsername());
            return new LoginResponse(false, "User not found");
        }
    }

    @GetMapping("/users")
    public List<User> listUsers() {
        return userRepository.findAll();
    }

    private static class LoginRequest {
        private String username;
        private String password;

        public String getUsername() {
            return username;
        }

        public void setUsername(String username) {
            this.username = username;
        }

        public String getPassword() {
            return password;
        }

        public void setPassword(String password) {
            this.password = password;
        }
    }

    private static class LoginResponse {
        private boolean success;
        private String message;

        public LoginResponse(boolean success, String message) {
            this.success = success;
            this.message = message;
        }

        public boolean isSuccess() {
            return success;
        }

        public void setSuccess(boolean success) {
            this.success = success;
        }

        public String getMessage() {
            return message;
        }

        public void setMessage(String message) {
            this.message = message;
        }
    }
}