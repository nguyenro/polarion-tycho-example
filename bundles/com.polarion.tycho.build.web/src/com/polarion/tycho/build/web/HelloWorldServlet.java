package com.polarion.tycho.build.web;

import java.io.IOException;
import java.io.Serial;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.polarion.platform.core.PlatformContext;
import com.polarion.tycho.build.service.Service;

public class HelloWorldServlet extends HttpServlet {

	@Serial
	private static final long serialVersionUID = -5329632843187790946L;

	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
		Service svc = PlatformContext.getPlatform().lookupService(Service.class);
		resp.getWriter().println(svc.doService());
	}
}
