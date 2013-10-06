class MainController < ApplicationController

	def index
	end

	def upload
		ip_address = request.remote_ip

		syllabi = ["1", "2", "3", "4", "5"]
		syllabi.each do |s|
			uploaded_io = params[s]
			if uploaded_io == nil
				next
			end
			path = File.dirname(Rails.root.join("public/uploads", ip_address.to_s, uploaded_io.original_filename))
			puts = "path = "+path
			unless File.directory?(path)
				FileUtils.mkdir_p(path)
			end
			File.open(Rails.root.join('public/uploads', ip_address, uploaded_io.original_filename), 'wb') do |file|
				file.write(uploaded_io.read)
			end
		end
		redirect_to dashboard_url
	end

	def dashboard
		@classes = ["18.404 Theory", "asdf"]
	end

	def processSyllabus
		ip_address = request.remote_ip
		command = "python script/2textconv/2txtconvert.py "+ip_address+" 2>&1"
		value = system(command)

		command ='python script/example.py '+ip_address+' 2>&1'
		kidoutput = `python script/example.py `+ip_address+` 2>&1`
		puts kidoutput
	end

	def about
	end

	def create     
		#What data comes back from OmniAuth?     
		@auth = request.env["omniauth.auth"]
		#Use the token from the data to request a list of calendars
		@token = @auth["credentials"]["token"]
		client = Google::APIClient.new
		client.authorization.access_token = @token
		service = client.discovered_api('calendar', 'v3')
		@result = client.execute(
		  :api_method => service.calendar_list.list,
		  :parameters => {},
		  :headers => {'Content-Type' => 'application/json'})
		puts @result
	end

end
