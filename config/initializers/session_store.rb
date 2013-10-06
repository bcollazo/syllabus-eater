# Be sure to restart your server when you modify this file.

# Your secret key for verifying cookie session data integrity.
# If you change this key, all old sessions will become invalid!
# Make sure the secret is at least 30 characters and all random, 
# no regular words or you'll be exposed to dictionary attacks.
ActionController::Base.session = {
  :key         => '_syllabus-eater_session',
  :secret      => 'd1893b49b7d0f454aa3a634512735e1860ee2f90692803b455756c544bc6acb1ef31ccecdcaa6044d1ae0bb7cd04caeb4482cd4041ac0a535da105f56b90e942'
}

# Use the database for sessions instead of the cookie-based default,
# which shouldn't be used to store highly confidential information
# (create the session table with "rake db:sessions:create")
# ActionController::Base.session_store = :active_record_store
