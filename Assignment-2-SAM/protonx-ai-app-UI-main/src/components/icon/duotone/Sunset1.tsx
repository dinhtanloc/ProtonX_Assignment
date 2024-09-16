import React, { SVGProps } from 'react';

const SvgSunset1 = (props: SVGProps<SVGSVGElement>) => {
	return (
		<svg viewBox='0 0 24 24' className='svg-icon' {...props}>
			<g fill='none' fillRule='evenodd'>
				<path d='M0 0h24v24H0z' />
				<path
					d='M8 16a4 4 0 118 0H8zm-4 2h16a1 1 0 010 2H4a1 1 0 010-2z'
					fill='currentColor'
				/>
				<path
					d='M19.5 13H21a1.5 1.5 0 010 3h-1.5a1.5 1.5 0 010-3zm-3.44-4.129l1.061-1.06a1.5 1.5 0 012.122 2.121l-1.061 1.06a1.5 1.5 0 01-2.121-2.12zM3 13h1.5a1.5 1.5 0 010 3H3a1.5 1.5 0 010-3zm9-8.5A1.5 1.5 0 0113.5 6v1.5a1.5 1.5 0 01-3 0V6A1.5 1.5 0 0112 4.5zM4.81 7.81a1.5 1.5 0 012.122 0l1.06 1.061a1.5 1.5 0 01-2.12 2.122L4.81 9.932a1.5 1.5 0 010-2.121z'
					fill='currentColor'
					opacity={0.3}
				/>
			</g>
		</svg>
	);
};

export default SvgSunset1;
