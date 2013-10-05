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
			unless File.directory?(path)
				FileUtils.mkdir_p(path)
			end
			File.open(Rails.root.join('public/uploads', ip_address, uploaded_io.original_filename), 'wb') do |file|
				file.write(uploaded_io.read)
			end
		end

		value = %x(cat 'public/upload/18510.pdf' 2>&1)
		puts "BRYAN ESSS EL CABALLO!! ", value

		redirect_to dashboard_url
	end

	def dashboard
		@classes = ["18.404 Theory of Computation",
			"6.046 Design and Analysis of Algorithms",
			"21M.645 Motion Theater"]
	end

end
