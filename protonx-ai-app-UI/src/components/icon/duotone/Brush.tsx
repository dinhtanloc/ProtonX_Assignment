import React, { SVGProps } from 'react';

const SvgBrush = (props: SVGProps<SVGSVGElement>) => {
	return (
		<svg viewBox='0 0 24 24' className='svg-icon' {...props}>
			<g fill='none' fillRule='evenodd'>
				<path d='M0 0h24v24H0z' />
				<path
					d='M16.058 5.116l2.121 2.12-2.475 4.597L20.3 9.358l1.768 1.768a.5.5 0 010 .707l-5.303 5.303-9.9-9.9 5.304-5.302a.5.5 0 01.707 0L14.643 3.7l-.707 2.122 2.122-.707z'
					fill='currentColor'
					opacity={0.3}
				/>
				<path
					d='M10.16 16.188l-3.292 4.703a2 2 0 01-3.052.267l-.958-.958a2 2 0 01.28-3.062l4.723-3.249-3.117-3.117a1 1 0 010-1.414l1.414-1.414 9.9 9.9-1.415 1.414a1 1 0 01-1.414 0l-3.07-3.07zm-5.416 3.07a1 1 0 101.414-1.415 1 1 0 00-1.414 1.415z'
					fill='currentColor'
				/>
			</g>
		</svg>
	);
};

export default SvgBrush;
