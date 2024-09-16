import React, { SVGProps } from 'react';

const SvgFryingPan = (props: SVGProps<SVGSVGElement>) => {
	return (
		<svg viewBox='0 0 24 24' className='svg-icon' {...props}>
			<g fill='none' fillRule='evenodd'>
				<path d='M0 0h24v24H0z' />
				<path
					d='M11 10.5l-.5.5-5.76-2.624a2.945 2.945 0 01-.826-4.798 2.908 2.908 0 014.72 1.01L11 10.5zM4.907 4.606a1.435 1.435 0 00-.045 2.029c.548.567 1.457.58 2.03.026a1.435 1.435 0 00.044-2.03 1.435 1.435 0 00-2.03-.025z'
					fill='currentColor'
					opacity={0.3}
				/>
				<path
					d='M9.94 19.925a7 7 0 119.899-9.9 7 7 0 01-9.9 9.9zM15 20.5a5.5 5.5 0 100-11 5.5 5.5 0 000 11zm0-1a4.5 4.5 0 110-9 4.5 4.5 0 010 9z'
					fill='currentColor'
				/>
			</g>
		</svg>
	);
};

export default SvgFryingPan;
